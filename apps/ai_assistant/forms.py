from django import forms
class CommandForm(forms.Form):
    command = forms.CharField(label="Comando", widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Digite um comando para o Odin..."}))
