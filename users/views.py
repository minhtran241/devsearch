from typing import List, Mapping, Any
from datetime import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from users.models import Profile, Message
from users.forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from users.utils import searchProfiles, paginateProfiles


def register_user(request: HttpRequest) -> HttpResponse:
    page: str = "register"
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            name_splitted: List[str] = user.first_name.split(" ")
            user.first_name = name_splitted[0].strip().capitalize()
            if len(name_splitted) > 1:
                user.last_name = name_splitted[1].strip().capitalize()
            user.username = user.username.strip().lower()
            user.save()
            messages.success(
                request=request, message="Your account was created successfully!"
            )
            login(request=request, user=user)
            return redirect(to="update-account")
        else:
            messages.error(
                request=request, message="An error has occurred during registration."
            )
    context: Mapping[str, Any] = {"page": page, "form": form}
    return render(
        request=request, template_name="users/login_register.html", context=context
    )


def login_user(request: HttpRequest) -> HttpResponse:
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
            return redirect(request.GET["next"] if "next" in request.GET else "account")
        else:
            messages.error(request=request, message="Incorrect username or password.")
    context: Mapping[str, Any] = {"page": page}
    return render(
        request=request, template_name="users/login_register.html", context=context
    )


@login_required(login_url="login")
def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request=request)
    messages.success(
        request=request,
        message="Sign out successfully!",
    )
    return redirect(to="login")


@login_required(login_url="login")
def account_user(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    context: Mapping[str:Any] = {"profile": profile}
    return render(request=request, template_name="users/account.html", context=context)


def profiles(request: HttpRequest) -> HttpResponse:
    profiles, search_query = searchProfiles(request=request)
    results: int = 9
    custom_range, profiles = paginateProfiles(
        request=request, profiles=profiles, results=results
    )
    context: Mapping[str, Any] = {
        "profiles": profiles,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request=request, template_name="users/profiles.html", context=context)


def profile(request: HttpRequest, pk) -> HttpResponse:
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")
    context: Mapping[str, Any] = {
        "profile": profile,
        "topSkills": top_skills,
        "otherSkills": other_skills,
    }
    return render(request=request, template_name="users/profile.html", context=context)


@login_required(login_url="login")
def update_account(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request=request,
                message="Your information updated successfully!",
            )
            return redirect(to="account")
    context: Mapping[str:Any] = {"form": form}
    return render(
        request=request, template_name="users/profile_form.html", context=context
    )


@login_required(login_url="login")
def create_skill(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(
                request=request,
                message="Skill added successfully!",
            )
            return redirect(to="account")
    context: Mapping[str:Any] = {"form": form}
    return render(
        request=request, template_name="users/skill_form.html", context=context
    )


@login_required(login_url="login")
def update_skill(request: HttpRequest, pk) -> HttpResponse:
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(
                request=request,
                message="Skill updated successfully!",
            )
            return redirect(to="account")
    context: Mapping[str:Any] = {"form": form}
    return render(
        request=request, template_name="users/skill_form.html", context=context
    )


@login_required(login_url="login")
def delete_skill(request: HttpRequest, pk) -> HttpResponse:
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        messages.success(
            request=request,
            message="Skill deleted successfully!",
        )
        return redirect("account")
    context: Mapping[str, Any] = {"object": skill}
    return render(
        request=request, template_name="delete_template.html", context=context
    )


@login_required(login_url="login")
def inbox(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    messages_list = profile.messages.all()
    unread_count: int | str = messages_list.filter(is_read=False).count()
    context: Mapping[str, Any] = {
        "messagesList": messages_list,
        "unreadCount": unread_count,
    }
    return render(request=request, template_name="users/inbox.html", context=context)


@login_required(login_url="login")
def view_message(request: HttpRequest, pk) -> HttpResponse:
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read is False:
        message.date_read = datetime.now()
        message.is_read = True
        message.save()
    context: Mapping[str, Any] = {"message": message}
    return render(request=request, template_name="users/message.html", context=context)


def send_message(request: HttpRequest, pk) -> HttpResponse:
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    if request.method == "POST":
        try:
            sender = request.user.profile
        except:
            sender = None
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            if sender:
                message.sender_name = sender.name
                message.email = sender.email
            message.save()
            messages.success(
                request=request,
                message="Message sent successfully!",
            )
            return redirect(to="profile", pk=recipient.id)
    context: Mapping[str, Any] = {"recipient": recipient, "form": form}
    return render(
        request=request, template_name="users/message_form.html", context=context
    )
