from django.urls import path
from .views import owner_panel

urlpatterns = [
    path("", owner_panel, name="owner_panel"),
]
