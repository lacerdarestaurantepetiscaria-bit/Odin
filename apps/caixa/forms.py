from django import forms

class CashOpenForm(forms.Form):
    opening_amount = forms.DecimalField(label="Valor de abertura", max_digits=10, decimal_places=2)
    notes = forms.CharField(label="Observações", required=False, widget=forms.Textarea(attrs={"rows": 2}))

class CashCloseForm(forms.Form):
    closing_amount = forms.DecimalField(label="Valor contado no fechamento", max_digits=10, decimal_places=2)
    notes = forms.CharField(label="Observações", required=False, widget=forms.Textarea(attrs={"rows": 2}))
