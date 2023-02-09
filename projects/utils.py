from typing import Any, Tuple
from django.http import HttpRequest
from django.db.models import Q

from projects.models import Project, Tag


def searchProjects(request: HttpRequest) -> Tuple[Any, str]:
    search_query: str = (
        request.GET.get("search_query") if request.GET.get("search_query") else ""
    )
    tags = Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query)
        | Q(owner__name__icontains=search_query)
        | Q(tags__in=tags)
    )
    return projects, search_query
