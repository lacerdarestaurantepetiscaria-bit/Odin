from django.urls import path
from .views import caixa_home

urlpatterns = [
    path("", caixa_home, name="caixa_home"),
]
