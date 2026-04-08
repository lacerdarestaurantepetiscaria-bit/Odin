from django.contrib import admin
from .models import CashSession

@admin.register(CashSession)
class CashSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "opening_amount", "closing_amount", "status", "opened_at", "closed_at")
    list_filter = ("status",)
