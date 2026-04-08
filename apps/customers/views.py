from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CustomerForm
from .models import Customer

def customer_list(request):
    return render(request, "customers/list.html", {"customers": Customer.objects.all()})

def customer_create(request):
    form = CustomerForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Cliente cadastrado com sucesso.")
        return redirect("customer_list")
    return render(request, "customers/form.html", {"form": form, "title": "Novo cliente"})
