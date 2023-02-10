from typing import Tuple, Any
from django.db.models import Q
from django.http import HttpRequest
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from users.models import Profile, Skill


def searchProfiles(request: HttpRequest) -> Tuple[Any, str]:
    search_query = (
        request.GET.get("search_query") if request.GET.get("search_query") else ""
    )
    skills = Skill.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | Q(skill__in=skills)
    )
    return profiles, search_query


def paginateProfiles(
    request: HttpRequest, profiles: Any, results: int
) -> Tuple[range, Any]:
    page: int | str = request.GET.get("page")  # current page
    paginator = Paginator(object_list=profiles, per_page=results)
    try:
        profiles = paginator.page(number=page)
    except PageNotAnInteger:  # query param page is not an integer
        page = 1  # direct user to the first page
        profiles = paginator.page(number=page)
    except EmptyPage:  # query param page out of bound
        page = paginator.num_pages  # direct user to the last page
        profiles = paginator.page(number=page)
    left_index: int = int(page) - 4 if int(page) > 4 else 1
    right_index: int = (
        int(page) + 5
        if int(page) + 5 <= paginator.num_pages + 1
        else paginator.num_pages + 1
    )
    custom_range = range(left_index, right_index)
    return custom_range, profiles
