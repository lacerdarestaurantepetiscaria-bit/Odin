from django.urls import path
from .views import supply_create, supply_list, supply_toggle

urlpatterns = [
    path("", supply_list, name="supply_list"),
    path("novo/", supply_create, name="supply_create"),
    path("<int:pk>/toggle/", supply_toggle, name="supply_toggle"),
]
