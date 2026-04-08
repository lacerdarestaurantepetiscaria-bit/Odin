from django.urls import path
from .views import entrega_home, entrega_status

urlpatterns = [
    path("", entrega_home, name="entrega_home"),
    path("<int:pk>/<str:status>/", entrega_status, name="entrega_status"),
]
