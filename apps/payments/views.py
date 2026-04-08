from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import PaymentForm
from .models import Payment

def payment_list(request):
    return render(request, "payments/list.html", {"payments": Payment.objects.select_related("order").all()})

def payment_create(request):
    form = PaymentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        payment = form.save()
        if payment.order and payment.order.status not in ["entregue", "cancelado"]:
            payment.order.status = "entregue"
            payment.order.save(update_fields=["status"])
        messages.success(request, "Pagamento registrado com sucesso. Pedido vinculado foi baixado.")
        return redirect("payment_list")
    return render(request, "payments/form.html", {"form": form, "title": "Novo pagamento"})
