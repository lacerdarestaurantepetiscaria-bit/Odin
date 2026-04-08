from django.shortcuts import get_object_or_404, redirect, render
from apps.orders.models import Order

def entrega_home(request):
    pedidos = Order.objects.filter(service_type="delivery").exclude(status="cancelado").prefetch_related("customer")
    return render(request, "entrega/home.html", {"pedidos": pedidos})

def entrega_status(request, pk, status):
    order = get_object_or_404(Order, pk=pk)
    if status in {"aberto", "preparo", "pronto", "entregue"}:
        order.status = status
        order.save(update_fields=["status"])
    return redirect("entrega_home")
