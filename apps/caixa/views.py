from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from .forms import CashCloseForm, CashOpenForm
from .models import CashSession
from apps.payments.models import Payment

def caixa_home(request):
    current = CashSession.objects.filter(status="aberto").first()
    sessions = CashSession.objects.all()[:10]
    open_form = CashOpenForm()
    close_form = CashCloseForm()

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "open":
            open_form = CashOpenForm(request.POST)
            if open_form.is_valid():
                if current:
                    messages.error(request, "Já existe um caixa aberto.")
                else:
                    CashSession.objects.create(
                        opening_amount=open_form.cleaned_data["opening_amount"],
                        notes=open_form.cleaned_data["notes"],
                    )
                    messages.success(request, "Caixa aberto com sucesso.")
                    return redirect("caixa_home")
        elif action == "close":
            close_form = CashCloseForm(request.POST)
            if close_form.is_valid():
                if not current:
                    messages.error(request, "Não existe caixa aberto.")
                else:
                    current.closing_amount = close_form.cleaned_data["closing_amount"]
                    current.notes = (current.notes + " | " if current.notes else "") + close_form.cleaned_data["notes"]
                    current.status = "fechado"
                    current.closed_at = timezone.now()
                    current.save()
                    messages.success(request, "Caixa fechado com sucesso.")
                    return redirect("caixa_home")

    totals = {
        "dinheiro": sum((p.amount for p in Payment.objects.filter(method="dinheiro")), 0),
        "cartao": sum((p.amount for p in Payment.objects.filter(method="cartao")), 0),
        "pix": sum((p.amount for p in Payment.objects.filter(method="pix")), 0),
        "voucher": sum((p.amount for p in Payment.objects.filter(method="voucher")), 0),
        "fiado": sum((p.amount for p in Payment.objects.filter(method="fiado")), 0),
    }

    return render(request, "caixa/home.html", {
        "current": current,
        "sessions": sessions,
        "open_form": open_form,
        "close_form": close_form,
        "totals": totals,
    })
