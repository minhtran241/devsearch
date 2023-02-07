from typing import List
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields: List[str] = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]
