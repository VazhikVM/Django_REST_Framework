from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from togo.serializers import ProjectSerializer, ToDoSerializer
from togo.models import Project, ToDo
from togo.filters import ProjectFilter, ToDoFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter
