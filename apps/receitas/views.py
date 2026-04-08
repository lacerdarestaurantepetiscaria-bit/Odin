from decimal import Decimal
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import RecipeItemForm
from .models import RecipeItem

def recipe_list(request):
    recipes = RecipeItem.objects.select_related("product", "supply").all()
    product_totals = {}
    for item in recipes:
        key = item.product.name
        product_totals[key] = product_totals.get(key, Decimal("0.00")) + item.estimated_cost
    return render(request, "receitas/list.html", {"recipes": recipes, "product_totals": product_totals})

def recipe_create(request):
    form = RecipeItemForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Ficha técnica adicionada com sucesso.")
        return redirect("recipe_list")
    return render(request, "receitas/form.html", {"form": form, "title": "Novo item de ficha técnica"})
