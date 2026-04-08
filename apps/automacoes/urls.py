from django.urls import path
from .views import automacoes_home

urlpatterns = [
    path("", automacoes_home, name="automacoes_home"),
]
