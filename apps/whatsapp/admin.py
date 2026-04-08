from django.contrib import admin
from .models import WhatsAppMessageLog

@admin.register(WhatsAppMessageLog)
class WhatsAppMessageLogAdmin(admin.ModelAdmin):
    list_display = ("sender_name", "sender_phone", "created_at")
    search_fields = ("sender_name", "sender_phone", "incoming_text")
