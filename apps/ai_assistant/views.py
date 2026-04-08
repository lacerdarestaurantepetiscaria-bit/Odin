from django.shortcuts import render
from .forms import CommandForm
from .services import process_command

def assistant_home(request):
    result = None
    form = CommandForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        result = process_command(form.cleaned_data["command"])
    return render(request, "ai_assistant/home.html", {"form": form, "result": result})
