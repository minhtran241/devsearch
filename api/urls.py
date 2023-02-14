from typing import List
from django.urls import path, URLPattern

from api import views

urlpatterns: List[URLPattern] = [
	path(route='', view=views.getRoutes)
]