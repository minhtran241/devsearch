from typing import List
from django.urls import path, URLPattern
from users import views

urlpatterns: List[URLPattern] = [
    path(route="", view=views.profiles, name="profiles"),
    path(route="profile/<str:pk>/", view=views.profile, name="profile"),
    path(route="register/", view=views.register_user, name="register"),
    path(route="login/", view=views.login_user, name="login"),
    path(route="logout/", view=views.logout_user, name="logout"),
]
