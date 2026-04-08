from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import SupplyForm
from .models import Supply

def supply_list(request):
    supplies = Supply.objects.all()
    return render(request, "estoque/list.html", {"supplies": supplies})

def supply_create(request):
    form = SupplyForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Insumo criado com sucesso.")
        return redirect("supply_list")
    return render(request, "estoque/form.html", {"form": form, "title": "Novo insumo"})

def supply_toggle(request, pk):
    supply = get_object_or_404(Supply, pk=pk)
    supply.is_active = not supply.is_active
    supply.save(update_fields=["is_active"])
    messages.success(request, f"Insumo {'habilitado' if supply.is_active else 'desabilitado'}.")
    return redirect("supply_list")
