from django.urls import path
from .views import order_create, order_list, order_status
urlpatterns = [
    path("", order_list, name="order_list"),
    path("novo/", order_create, name="order_create"),
    path("<int:pk>/status/<str:status>/", order_status, name="order_status"),
]
