from django.urls import path
from .views import recipe_create, recipe_list

urlpatterns = [
    path("", recipe_list, name="recipe_list"),
    path("novo/", recipe_create, name="recipe_create"),
]
