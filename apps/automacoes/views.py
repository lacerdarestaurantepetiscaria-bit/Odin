from django.contrib import messages
from django.shortcuts import redirect, render
from apps.estoque.models import Supply
from apps.products.models import Product

def automacoes_home(request):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "desativar_indisponiveis":
            affected = 0
            low_names = {s.name.lower() for s in Supply.objects.filter(quantity__lte=0)}
            for product in Product.objects.filter(is_active=True):
                product_name = product.name.lower()
                if any(name in product_name for name in low_names if name):
                    product.is_active = False
                    product.save(update_fields=["is_active"])
                    affected += 1
            messages.success(request, f"Automação executada. Produtos desativados: {affected}.")
            return redirect("automacoes_home")
    low_supplies = Supply.objects.filter(quantity__lte=0)
    return render(request, "automacoes/home.html", {"low_supplies": low_supplies})
