from django.urls import path
from .views import alert_center

urlpatterns = [
    path("", alert_center, name="alert_center"),
]
