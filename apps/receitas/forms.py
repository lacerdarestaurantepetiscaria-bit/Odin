from django import forms
from .models import RecipeItem

class RecipeItemForm(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = ["product", "supply", "quantity_used"]
