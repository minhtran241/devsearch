from typing import List
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile, Skill


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels = {
            "first_name": "Name",
        }

    def __init__(self, *arg, **kwargs):
        super(CustomUserCreationForm, self).__init__(*arg, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "email",
            "username",
            "location",
            "short_intro",
            "bio",
            "profile_image",
            "social_website",
            "social_github",
            "social_stackoverflow",
            "social_linkedin",
            "social_twitter",
            "social_youtube",
        ]

    def __init__(self, *arg, **kwargs):
        super(ProfileForm, self).__init__(*arg, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]

    def __init__(self, *arg, **kwargs):
        super(SkillForm, self).__init__(*arg, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
