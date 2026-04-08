from django.shortcuts import render
from apps.estoque.models import Supply
from apps.orders.models import Order

def alert_center(request):
    low_supplies = Supply.objects.filter(quantity__lte=0) | Supply.objects.filter(quantity__lte=__import__('django.db.models').db.models.F("minimum_quantity"))
    delayed_orders = Order.objects.filter(status__in=["aberto", "preparo"]).order_by("created_at")[:12]
    return render(request, "alerts/home.html", {
        "low_supplies": low_supplies.distinct(),
        "delayed_orders": delayed_orders,
    })
