from typing import List, Mapping
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ProjectSerializer
from projects.models import Project


@api_view(http_method_names=["GET"])
def getRoutes(request: HttpRequest) -> Response:
    routes: List[Mapping[str, str]] = [
        {"GET": "/api/projects"},
        {"GET": "/api/projects/id"},
        {"POST": "/api/projects/id/vote"},
        {"POST": "/api/users/token"},
        {"POST": "/api/users/token/refresh"},
    ]
    return Response(data=routes)


@api_view(http_method_names=["GET"])
def getProjects(request: HttpRequest) -> Response:
    projects = Project.objects.all()
    serializer = ProjectSerializer(instance=projects, many=True)
    return Response(data=serializer.data)


@api_view(http_method_names=["GET"])
def getProject(request: HttpRequest, pk: str):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project, many=False)
    return Response(data=serializer.data)
