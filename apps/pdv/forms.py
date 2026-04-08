from django import forms

class PDVCheckoutForm(forms.Form):
    customer_name = forms.CharField(required=False, label="Cliente")
    table_number = forms.CharField(required=False, label="Mesa")
    service_type = forms.ChoiceField(
        choices=[
            ("mesa", "Mesa"),
            ("balcao", "Balcão"),
            ("delivery", "Delivery"),
            ("retirada", "Retirada"),
        ],
        initial="balcao",
        label="Atendimento"
    )
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 2}), label="Observações")
    items_json = forms.CharField(widget=forms.HiddenInput())
