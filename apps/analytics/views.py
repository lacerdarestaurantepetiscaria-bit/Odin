from collections import defaultdict
from decimal import Decimal
from django.shortcuts import render
from apps.orders.models import Order
from apps.payments.models import Payment
from apps.consumo.models import StockConsumption
from apps.estoque.models import Supply

def owner_panel(request):
    orders = Order.objects.all()
    payments = Payment.objects.all()
    total_orders = orders.count()
    total_revenue = sum((p.amount for p in payments), Decimal("0.00"))
    ticket_medio = (total_revenue / total_orders) if total_orders else Decimal("0.00")

    product_counter = defaultdict(int)
    for order in orders.prefetch_related("items", "items__product"):
        for item in order.items.all():
            product_counter[item.product.name] += item.quantity
    top_product = max(product_counter.items(), key=lambda x: x[1])[0] if product_counter else "-"

    low_supplies = Supply.objects.filter(quantity__lte=0) | Supply.objects.filter(quantity__lte=__import__('django.db.models').db.models.F("minimum_quantity"))
    low_supplies = list(low_supplies.distinct()[:8])

    total_consumption = sum((c.quantity_consumed for c in StockConsumption.objects.all()), Decimal("0.00"))

    context = {
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "ticket_medio": ticket_medio,
        "top_product": top_product,
        "low_supplies": low_supplies,
        "total_consumption": total_consumption,
        "recent_orders": orders.order_by("-created_at")[:10],
        "recent_payments": payments.order_by("-created_at")[:10],
    }
    return render(request, "analytics/owner_panel.html", context)
