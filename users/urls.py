from typing import List
from django.urls import path, URLPattern
from users import views

urlpatterns: List[URLPattern] = [path(route="", view=views.profiles, name="profiles")]
