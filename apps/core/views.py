from decimal import Decimal
from django.shortcuts import render
from apps.orders.models import Order
from apps.payments.models import Payment

def dashboard(request):
    orders = Order.objects.order_by("-created_at")[:10]
    total_orders = Order.objects.count()
    total_revenue = sum((p.amount for p in Payment.objects.all()), Decimal("0.00"))
    return render(request, "core/dashboard.html", {
        "orders": orders,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
    })
