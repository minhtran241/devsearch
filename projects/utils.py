from typing import Any, Tuple
from django.http import HttpRequest
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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


def paginateProjects(
    request: HttpRequest, projects: Any, results: int
) -> Tuple[range, Any]:
    page: int | str = request.GET.get("page")  # current page
    paginator = Paginator(object_list=projects, per_page=results)
    try:
        projects = paginator.page(number=page)
    except PageNotAnInteger:  # query param page is not an integer
        page = 1  # direct user to the first page
        projects = paginator.page(number=page)
    except EmptyPage:  # query param page out of bound
        page = paginator.num_pages  # direct user to the last page
        projects = paginator.page(number=page)
    left_index: int = int(page) - 4 if int(page) > 4 else 1
    right_index: int = (
        int(page) + 5
        if int(page) + 5 <= paginator.num_pages + 1
        else paginator.num_pages + 1
    )
    custom_range = range(left_index, right_index)
    return custom_range, projects
