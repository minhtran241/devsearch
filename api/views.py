from typing import List, Mapping
from django.http import HttpRequest
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from api.serializers import ProjectSerializer
from projects.models import Project, Review


@api_view(http_method_names=["GET"])
def getRoutes(request: HttpRequest) -> Response:
    routes: List[Mapping[str, str]] = [
        {"GET": "/api/projects"},
        {"GET": "/api/projects/id"},
        {"POST": "/api/projects/id/vote"},
        {"POST": "/api/users/token"},
        {"POST": "/api/users/token/refresh"},
        {"POST": "/api/users/token/verify"},
    ]
    return Response(data=routes)


@api_view(http_method_names=["GET"])
def getProjects(request: HttpRequest) -> Response:
    projects = Project.objects.all()
    serializer = ProjectSerializer(instance=projects, many=True)
    return Response(data=serializer.data)


@api_view(http_method_names=["GET"])
def getProject(request: HttpRequest, pk: str) -> Response:
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project, many=False)
    return Response(data=serializer.data)


@api_view(http_method_names=["POST", "PUT"])
@permission_classes(permission_classes=[IsAuthenticated])
def projectVote(request: HttpRequest, pk: str) -> Response:
    project = Project.objects.get(id=pk)
    user_profile = request.user.profile
    data = request.data
    review, created = Review.objects.get_or_create(owner=user_profile, project=project)
    review.value = data["value"]
    review.save()
    project.get_vote_count
    serializer = ProjectSerializer(instance=project, many=False)
    return Response(serializer.data)
