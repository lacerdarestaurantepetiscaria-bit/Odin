from django.contrib import admin
from .models import RecipeItem

@admin.register(RecipeItem)
class RecipeItemAdmin(admin.ModelAdmin):
    list_display = ("product", "supply", "quantity_used")
    list_filter = ("product", "supply")
