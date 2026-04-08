from django.contrib import admin
from .models import Supply

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "unit", "quantity", "minimum_quantity", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name",)
