import re
from decimal import Decimal
from apps.customers.models import Customer
from apps.orders.models import Order, OrderItem
from apps.products.models import Product
from apps.consumo.services import apply_stock_consumption

def _normalize(text: str) -> str:
    mapping = {
        "á":"a","à":"a","â":"a","ã":"a",
        "é":"e","ê":"e",
        "í":"i",
        "ó":"o","ô":"o","õ":"o",
        "ú":"u","ç":"c",
    }
    text = text.lower()
    for k, v in mapping.items():
        text = text.replace(k, v)
    return text

def _extract_qty(message: str):
    norm = _normalize(message)
    if "dois " in norm or "2 " in norm:
        return 2
    if "tres " in norm or "3 " in norm:
        return 3
    return 1

def parse_order_message(message: str):
    norm = _normalize(message)
    products = Product.objects.filter(is_active=True)
    matched = []
    for product in products:
        product_norm = _normalize(product.name)
        tokens = [t for t in product_norm.split() if len(t) > 2]
        direct = product_norm in norm
        partial = sum(1 for t in tokens if t in norm) >= max(1, min(2, len(tokens)))
        alias = False

        alias_terms = []
        if "frango" in product_norm and ("empanado" in norm or "milanesa" in norm):
            alias = True
        if "figado" in product_norm and "figado" in norm:
            alias = True
        if "pure" in product_norm and "pure" in norm:
            alias = True
        if "arroz" in product_norm and "arroz" in norm:
            alias = True
        if "feijao" in product_norm and "feijao" in norm:
            alias = True
        if "salada" in product_norm and "salada" in norm:
            alias = True

        if direct or partial or alias:
            matched.append(product)

    # remove duplicates preserving order
    uniq = []
    seen = set()
    for p in matched:
        if p.id not in seen:
            uniq.append(p)
            seen.add(p.id)

    qty = _extract_qty(message)
    items = [{"product": p, "qty": qty if p.category == "carne" else 1} for p in uniq]
    total = sum((item["product"].price * item["qty"] for item in items), Decimal("0.00"))

    summary_lines = []
    for item in items:
        summary_lines.append(f"{item['qty']}x {item['product'].name} - R$ {item['product'].price}")
    summary = "\n".join(summary_lines) if summary_lines else "Nenhum item reconhecido."
    return {
        "items": items,
        "total": total,
        "summary": summary,
        "recognized": bool(items),
    }

def create_order_from_whatsapp(sender_name, sender_phone, message):
    parsed = parse_order_message(message)
    customer = None
    if sender_name or sender_phone:
        customer, _ = Customer.objects.get_or_create(
            phone=sender_phone or "",
            defaults={"name": sender_name or sender_phone or "Cliente WhatsApp"}
        )
        if sender_name and customer.name != sender_name:
            customer.name = sender_name
            customer.save(update_fields=["name"])

    order = None
    if parsed["recognized"]:
        order = Order.objects.create(
            customer=customer,
            service_type="delivery",
            status="aberto",
            notes=f"Pedido criado via simulador WhatsApp: {message}",
        )
        for item in parsed["items"]:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["qty"],
                unit_price=item["product"].price,
            )
        apply_stock_consumption(order)

    response = (
        f"Perfeito. Montei seu pedido.\n{parsed['summary']}\n"
        f"Total parcial: R$ {parsed['total']}."
        if parsed["recognized"] else
        "Não consegui reconhecer itens suficientes do cardápio. Tente escrever os nomes dos produtos cadastrados."
    )
    return parsed, order, response
