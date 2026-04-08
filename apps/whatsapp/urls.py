from django.urls import path
from .views import whatsapp_home

urlpatterns = [
    path("", whatsapp_home, name="whatsapp_home"),
]
