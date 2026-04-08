from django.contrib import admin
from .models import StockConsumption

@admin.register(StockConsumption)
class StockConsumptionAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "supply", "quantity_consumed", "created_at")
    list_filter = ("product", "supply")
