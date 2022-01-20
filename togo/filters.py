from django_filters import rest_framework as filters
from togo.models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name', 'users']


class ToDoFilter(filters.FilterSet):
    text = filters.CharFilter(lookup_expr='contains')
    create = filters.DateTimeFilter(field_name="create", lookup_expr='gte', label='Больше или равно даты создания')

    class Meta:
        model = ToDo
        fields = ['text', 'is_active', 'create']
