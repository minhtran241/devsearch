from django.shortcuts import render


def profiles(request):
    return render(request=request, template_name="users/profiles.html")
