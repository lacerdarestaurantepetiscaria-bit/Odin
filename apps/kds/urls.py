from django.urls import path
from .views import kds_home, kds_move

urlpatterns = [
    path("", kds_home, name="kds_home"),
    path("<int:pk>/<str:status>/", kds_move, name="kds_move"),
]
