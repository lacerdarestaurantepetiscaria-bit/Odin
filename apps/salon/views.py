from django.shortcuts import render
from apps.orders.models import Order

def salon_home(request):
    tables = []
    for n in range(1, 21):
        current = Order.objects.filter(table_number=str(n)).exclude(status__in=["entregue", "cancelado"]).order_by("-created_at").first()
        status = current.status if current else "livre"
        total = current.total if current else 0
        item_count = sum(item.quantity for item in current.items.all()) if current else 0
        tables.append({
            "number": n,
            "order": current,
            "status": status,
            "total": total,
            "item_count": item_count,
        })
    return render(request, "salon/home.html", {"tables": tables})
