from django.shortcuts import render
from .forms import WhatsAppSimulatorForm
from .models import WhatsAppMessageLog
from .services import create_order_from_whatsapp, parse_order_message

def whatsapp_home(request):
    form = WhatsAppSimulatorForm(request.POST or None)
    result = None

    if request.method == "POST" and form.is_valid():
        sender_name = form.cleaned_data["sender_name"]
        sender_phone = form.cleaned_data["sender_phone"]
        message = form.cleaned_data["message"]
        create_order = form.cleaned_data["create_order"]

        if create_order:
            parsed, order, response = create_order_from_whatsapp(sender_name, sender_phone, message)
        else:
            parsed = parse_order_message(message)
            order = None
            response = (
                f"Interpretação simulada:\n{parsed['summary']}\nTotal parcial: R$ {parsed['total']}."
                if parsed["recognized"] else
                "Não consegui reconhecer itens suficientes do cardápio."
            )

        WhatsAppMessageLog.objects.create(
            sender_name=sender_name,
            sender_phone=sender_phone,
            incoming_text=message,
            parsed_summary=parsed["summary"],
            generated_response=response,
        )

        result = {
            "parsed": parsed,
            "order": order,
            "response": response,
        }

    logs = WhatsAppMessageLog.objects.all()[:12]
    return render(request, "whatsapp/home.html", {
        "form": form,
        "result": result,
        "logs": logs,
    })
