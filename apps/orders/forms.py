from django import forms
from apps.products.models import Product
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer", "table_number", "service_type", "status", "notes"]

class QuickOrderItemForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.filter(is_active=True), label="Produto")
    quantity = forms.IntegerField(min_value=1, initial=1, label="Quantidade")
