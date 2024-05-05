from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit-todo", views.submit_todo, name="submit-todo"),
]
