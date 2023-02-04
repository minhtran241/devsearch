from typing import List
from django.urls import path
from . import views

urlpatterns: List = [
    path(route="", view=views.projects, name="projects"),
    path(route="project/<str:pk>", view=views.project, name="project"),
    path(route="create-project/", view=views.create_project, name="create-project"),
]
