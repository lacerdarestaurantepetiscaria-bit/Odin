import re
from decimal import Decimal
from apps.payments.models import Payment
from apps.products.models import Product
from apps.estoque.models import Supply
from apps.orders.models import Order
from apps.caixa.models import CashSession

def process_command(command: str) -> dict:
    text = command.strip().lower()
    payment_match = re.search(r"pagou\s+(\d+[\.,]?\d*)\s+no\s+(cart[aã]o|pix|dinheiro|voucher|fiado)", text)
    if payment_match:
        amount = Decimal(payment_match.group(1).replace(",", "."))
        raw = payment_match.group(2)
        method = {"cartão":"cartao","cartao":"cartao","pix":"pix","dinheiro":"dinheiro","voucher":"voucher","fiado":"fiado"}[raw]
        payment = Payment.objects.create(method=method, amount=amount, notes=f"Lançado por comando: {command}")
        return {"ok": True, "message": f"Pagamento de R$ {payment.amount} registrado em {payment.get_method_display()}."}
    m = re.search(r"desabilitar\s+(.+)", text)
    if m:
        name = m.group(1).strip()
        product = Product.objects.filter(name__iexact=name).first()
        if product:
            product.is_active = False
            product.save(update_fields=["is_active"])
            return {"ok": True, "message": f"Produto {product.name} desabilitado."}
        return {"ok": False, "message": f"Produto '{name}' não encontrado."}
    m = re.search(r"habilitar\s+(.+)", text)
    if m:
        name = m.group(1).strip()
        product = Product.objects.filter(name__iexact=name).first()
        if product:
            product.is_active = True
            product.save(update_fields=["is_active"])
            return {"ok": True, "message": f"Produto {product.name} habilitado."}
        return {"ok": False, "message": f"Produto '{name}' não encontrado."}

    stock_off_match = re.search(r"estoque de\s+(.+?)\s+acabou", text)
    if stock_off_match:
        name = stock_off_match.group(1).strip()
        supply = Supply.objects.filter(name__iexact=name).first()
        if supply:
            supply.quantity = 0
            supply.save(update_fields=["quantity"])
            return {"ok": True, "message": f"Estoque de {supply.name} zerado com sucesso."}
        return {"ok": False, "message": f"Insumo '{name}' não encontrado."}

    stock_query_match = re.search(r"quanto tem de\s+(.+)", text)
    if stock_query_match:
        name = stock_query_match.group(1).strip()
        supply = Supply.objects.filter(name__iexact=name).first()
        if supply:
            return {"ok": True, "message": f"{supply.name}: {supply.quantity} {supply.get_unit_display()} em estoque."}
        return {"ok": False, "message": f"Insumo '{name}' não encontrado."}


    if "quanto vendi hoje" in text or "quanto vendeu hoje" in text:
        total = sum((p.amount for p in Payment.objects.all()), Decimal("0.00"))
        return {"ok": True, "message": f"Total vendido registrado: R$ {total}."}

    if "produto mais vendido" in text:
        counter = {}
        for order in Order.objects.prefetch_related("items", "items__product").all():
            for item in order.items.all():
                counter[item.product.name] = counter.get(item.product.name, 0) + item.quantity
        if counter:
            top_name = max(counter, key=counter.get)
            return {"ok": True, "message": f"Produto mais vendido até agora: {top_name}."}
        return {"ok": False, "message": "Ainda não há vendas suficientes para calcular o produto mais vendido."}

    if "estoque" in text and "baixo" in text:
        low = Supply.objects.filter(quantity__lte=0) | Supply.objects.filter(quantity__lte=__import__('django.db.models').db.models.F("minimum_quantity"))
        names = [s.name for s in low.distinct()[:10]]
        if names:
            return {"ok": True, "message": "Insumos com estoque baixo: " + ", ".join(names) + "."}
        return {"ok": True, "message": "Nenhum insumo com estoque baixo no momento."}

    if "fecha o caixa" in text or "fechar caixa" in text:
        current = CashSession.objects.filter(status="aberto").first()
        if not current:
            return {"ok": False, "message": "Não existe caixa aberto para fechar."}
        current.status = "fechado"
        current.closed_at = __import__('django.utils.timezone').utils.timezone.now()
        current.save(update_fields=["status", "closed_at"])
        return {"ok": True, "message": f"Caixa #{current.id} fechado com sucesso pelo Odin."}

    if "quanto vendeu hoje" in text:
        total = sum((p.amount for p in Payment.objects.all()), Decimal("0.00"))
        return {"ok": True, "message": f"Total vendido registrado: R$ {total}."}
    return {"ok": False, "message": "Comando ainda não reconhecido. Exemplos: cliente pagou 60 no cartão | desabilitar arroz branco | quanto vendeu hoje"}
