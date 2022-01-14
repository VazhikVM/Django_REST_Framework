from rest_framework.viewsets import ModelViewSet
from togo.serializers import ProjectSerializer, ToDoSerializer
from togo.models import Project, ToDo


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
