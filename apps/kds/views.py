from django.shortcuts import get_object_or_404, redirect, render
from apps.orders.models import Order

def kds_home(request):
    preparo = Order.objects.filter(status="preparo").prefetch_related("items", "items__product")
    pronto = Order.objects.filter(status="pronto").prefetch_related("items", "items__product")
    aberto = Order.objects.filter(status="aberto").prefetch_related("items", "items__product")
    return render(request, "kds/home.html", {
        "aberto": aberto,
        "preparo": preparo,
        "pronto": pronto,
    })

def kds_move(request, pk, status):
    order = get_object_or_404(Order, pk=pk)
    if status in {"aberto", "preparo", "pronto", "entregue"}:
        order.status = status
        order.save(update_fields=["status"])
    return redirect("kds_home")
