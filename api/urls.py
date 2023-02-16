from typing import List
from django.urls import path, URLPattern
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api import views

urlpatterns: List[URLPattern] = [
    path(
        route="users/token/",
        view=TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        route="users/token/refresh/",
        view=TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        route="users/token/verify/", view=TokenVerifyView.as_view(), name="token_verify"
    ),
    path(route="", view=views.getRoutes),
    path(route="projects/", view=views.getProjects),
    path(route="projects/<str:pk>/", view=views.getProject),
    path(route="projects/<str:pk>/vote/", view=views.projectVote),
    path(route="remove-tag/", view=views.removeTag),
]
