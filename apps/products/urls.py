from django.urls import path
from .views import product_create, product_list, product_toggle
urlpatterns = [
    path("", product_list, name="product_list"),
    path("novo/", product_create, name="product_create"),
    path("<int:pk>/toggle/", product_toggle, name="product_toggle"),
]
