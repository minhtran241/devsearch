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

    def __init__(self, *arg, **kwargs):
        super(CustomUserCreationForm, self).__init__(*arg, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
