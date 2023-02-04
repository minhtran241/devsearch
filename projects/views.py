from typing import Mapping, Any
from django.shortcuts import render
from django.http import HttpResponse

from projects.models import Project
from projects.forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context: Mapping[str, Any] = {"projects": projects}
    return render(
        request=request, template_name="projects/projects.html", context=context
    )


def project(request, pk):
    project = Project.objects.get(id=pk)
    context: Mapping[str, Any] = {"project": project}
    return render(
        request=request,
        template_name="projects/single-project.html",
        context=context,
    )


def create_project(request):
    form = ProjectForm()
    context: Mapping[str, Any] = {"form": form}
    return render(
        request=request, template_name="projects/project_form.html", context=context
    )
