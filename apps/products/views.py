from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductForm
from .models import Product

def product_list(request):
    return render(request, "products/list.html", {"products": Product.objects.all()})

def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Produto criado com sucesso.")
        return redirect("product_list")
    return render(request, "products/form.html", {"form": form, "title": "Novo produto"})

def product_toggle(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_active = not product.is_active
    product.save(update_fields=["is_active"])
    messages.success(request, f"Produto {'habilitado' if product.is_active else 'desabilitado'}.")
    return redirect("product_list")
