from django.urls import path
from .views import assistant_home
urlpatterns = [path("", assistant_home, name="assistant_home")]
