from django.urls import path
from .views import customer_create, customer_list
urlpatterns = [
    path("", customer_list, name="customer_list"),
    path("novo/", customer_create, name="customer_create"),
]
