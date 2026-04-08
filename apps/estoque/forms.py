from django import forms
from .models import Supply

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ["name", "category", "unit", "quantity", "cost", "minimum_quantity", "is_active"]
