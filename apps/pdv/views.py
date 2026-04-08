import json
from decimal import Decimal
from django.contrib import messages
from django.shortcuts import redirect, render
from apps.customers.models import Customer
from apps.orders.models import Order, OrderItem
from apps.products.models import Product
from .forms import PDVCheckoutForm
from apps.consumo.services import apply_stock_consumption

def pdv_home(request):
    products = Product.objects.filter(is_active=True).order_by("category", "name")
    categories = []
    seen = set()
    for product in products:
        if product.category not in seen:
            seen.add(product.category)
            categories.append((product.category, product.get_category_display()))
    form = PDVCheckoutForm()

    if request.method == "POST":
        form = PDVCheckoutForm(request.POST)
        if form.is_valid():
            try:
                items = json.loads(form.cleaned_data["items_json"])
            except Exception:
                items = []

            valid_items = []
            for item in items:
                try:
                    product = Product.objects.get(id=item["id"], is_active=True)
                    qty = int(item["qty"])
                    if qty > 0:
                        valid_items.append((product, qty))
                except Exception:
                    pass

            if not valid_items:
                messages.error(request, "Adicione pelo menos um item no pedido.")
                return render(request, "pdv/home.html", {
                    "products": products,
                    "categories": categories,
                    "form": form,
                })

            customer = None
            customer_name = form.cleaned_data["customer_name"].strip()
            if customer_name:
                customer, _ = Customer.objects.get_or_create(name=customer_name)

            order = Order.objects.create(
                customer=customer,
                table_number=form.cleaned_data["table_number"],
                service_type=form.cleaned_data["service_type"],
                status="aberto",
                notes=form.cleaned_data["notes"],
            )

            for product, qty in valid_items:
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=qty,
                    unit_price=product.price,
                )

            apply_stock_consumption(order)
            messages.success(request, f"Pedido #{order.id} criado no PDV com sucesso. Estoque baixado quando houver ficha técnica.")
            return redirect("pdv_home")

    return render(request, "pdv/home.html", {
        "products": products,
        "categories": categories,
        "form": form,
    })
