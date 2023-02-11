from typing import List
from django.urls import path, URLPattern
from users import views

urlpatterns: List[URLPattern] = [
    path(route="", view=views.profiles, name="profiles"),
    path(route="profile/<str:pk>/", view=views.profile, name="profile"),
    path(route="register/", view=views.register_user, name="register"),
    path(route="login/", view=views.login_user, name="login"),
    path(route="logout/", view=views.logout_user, name="logout"),
    path(route="account/", view=views.account_user, name="account"),
    path(route="update-account/", view=views.update_account, name="update-account"),
    path(route="create-skill/", view=views.create_skill, name="create-skill"),
    path(route="update-skill/<str:pk>/", view=views.update_skill, name="update-skill"),
    path(route="delete-skill/<str:pk>/", view=views.delete_skill, name="delete-skill"),
		path(route='inbox/', view=views.inbox, name='inbox'),
		path(route='message/<str:pk>/', view=views.view_message, name='message'),
		path(route='send-message/<str:pk>/', view=views.send_message, name='send-message')
]
