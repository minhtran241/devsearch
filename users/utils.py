from typing import Tuple, Any
from django.db.models import Q
from django.http import HttpRequest

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
