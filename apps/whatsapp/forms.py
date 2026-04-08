from django import forms

class WhatsAppSimulatorForm(forms.Form):
    sender_name = forms.CharField(label="Nome do cliente", required=False)
    sender_phone = forms.CharField(label="Telefone", required=False)
    message = forms.CharField(label="Mensagem recebida", widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Ex.: quero arroz, feijão, purê e fígado"}))
    create_order = forms.BooleanField(label="Gerar pedido automaticamente", required=False, initial=True)
