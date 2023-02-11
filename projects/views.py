from typing import Mapping, Any
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from projects.models import Project
from projects.forms import ProjectForm, ReviewForm
from projects.utils import searchProjects, paginateProjects


def projects(request):
    projects, search_query = searchProjects(request=request)
    results: int = 9  # how many results per page
    custom_range, projects = paginateProjects(
        request=request, projects=projects, results=results
    )
    context: Mapping[str, Any] = {
        "projects": projects,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(
        request=request, template_name="projects/projects.html", context=context
    )


def project(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()
            # Update project vote_count
            project.get_vote_count
            messages.success(
                request=request,
                message="Review recorded!",
            )
            return redirect(to="project", pk=project.id)
    context: Mapping[str, Any] = {"project": project, "form": form}
    return render(
        request=request,
        template_name="projects/single-project.html",
        context=context,
    )


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(
                request=request,
                message="Project created successfully!",
            )
            return redirect("account")
    context: Mapping[str, Any] = {"form": form}
    return render(
        request=request, template_name="projects/project_form.html", context=context
    )


@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(
                request=request,
                message="Project updated successfully!",
            )
            return redirect("account")
    context: Mapping[str, Any] = {"form": form}
    return render(
        request=request, template_name="projects/project_form.html", context=context
    )


@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        messages.success(
            request=request,
            message="Project deleted successfully!",
        )
        return redirect("projects")
    context: Mapping[str, Any] = {"object": project}
    return render(
        request=request, template_name="delete_template.html", context=context
    )
