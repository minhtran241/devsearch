from typing import List, Mapping
from django.http import HttpRequest, JsonResponse


def getRoutes(request: HttpRequest):
    routes: List[Mapping[str, str]] = [
        {"GET": "/api/projects"},
        {"GET": "/api/projects/id"},
        {"POST": "/api/projects/id/vote"},
        {"POST": "/api/users/token"},
        {"POST": "/api/users/token/refresh"},
    ]
    return JsonResponse(data=routes, safe=False)
