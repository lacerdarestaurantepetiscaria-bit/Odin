from django.urls import path
from .views import salon_home

urlpatterns = [
    path("", salon_home, name="salon_home"),
]
