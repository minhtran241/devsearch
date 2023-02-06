from typing import Mapping, Any
from django.shortcuts import render

from users.models import Profile


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
