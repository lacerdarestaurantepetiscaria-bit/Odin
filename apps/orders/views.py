from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import OrderForm, QuickOrderItemForm
from .models import Order, OrderItem

def order_list(request):
    return render(request, "orders/list.html", {"orders": Order.objects.prefetch_related("items","customer").all()})

def order_create(request):
    form = OrderForm(request.POST or None)
    item_form = QuickOrderItemForm(request.POST or None)
    if request.method == "POST" and form.is_valid() and item_form.is_valid():
        order = form.save()
        product = item_form.cleaned_data["product"]
        quantity = item_form.cleaned_data["quantity"]
        OrderItem.objects.create(order=order, product=product, quantity=quantity, unit_price=product.price)
        messages.success(request, "Pedido criado com sucesso.")
        return redirect("order_list")
    return render(request, "orders/form.html", {"form": form, "item_form": item_form, "title": "Novo pedido"})

def order_status(request, pk, status):
    order = get_object_or_404(Order, pk=pk)
    if status in {"aberto","preparo","pronto","entregue","cancelado"}:
        order.status = status
        order.save(update_fields=["status"])
        messages.success(request, f"Pedido #{order.pk} atualizado para {status}.")
    return redirect("order_list")
