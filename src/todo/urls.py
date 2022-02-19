from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-task/", views.add_task, name="add-task"),
    path("update-task/<int:id>", views.update_task, name="update-task"),
    path("delete-task/<int:id>", views.delete_task, name="delete-task"),
    path("complet-task/<int:id>", views.complet_task, name="complet-task"),
]