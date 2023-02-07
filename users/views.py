from typing import Mapping, Any
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User

from users.models import Profile
from users.forms import CustomUserCreationForm


def register_user(request):
    page: str = "register"
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = user.first_name.strip().capitalize()
            user.last_name = user.last_name.strip().capitalize()
            user.username = user.username.strip().lower()
            user.save()
            messages.success(
                request=request, message="Account was created successfully!"
            )
            login(request=request, user=user)
            return redirect(to="profiles")
        else:
            messages.error(
                request=request, message="An error has occurred during registration"
            )
    context: Mapping[str, Any] = {"page": page, "form": form}
    return render(
        request=request, template_name="users/login_register.html", context=context
    )


def login_user(request):
    page: str = "login"
    if request.user.is_authenticated:
        return redirect(to="profiles")
    if request.method == "POST":
        username: str = request.POST["username"]
        password: str = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(
                request=request,
                message="This username is not registered.",
            )
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request=request, user=user)
            return redirect(to="profiles")
        else:
            messages.error(request=request, message="Incorrect username or password.")
    context: Mapping[str, Any] = {"page": page}
    return render(
        request=request, template_name="users/login_register.html", context=context
    )


def logout_user(request):
    logout(request=request)
    messages.success(
        request=request,
        message="Sign out successfully!",
    )
    return redirect(to="login")


def profiles(request):
    profiles = Profile.objects.all()
    context: Mapping[str, Any] = {"profiles": profiles}
    return render(request=request, template_name="users/profiles.html", context=context)


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact="")[:5]
    other_skills = profile.skill_set.filter(description="")
    context: Mapping[str, Any] = {
        "profile": profile,
        "topSkills": top_skills,
        "otherSkills": other_skills,
    }
    return render(request=request, template_name="users/profile.html", context=context)
