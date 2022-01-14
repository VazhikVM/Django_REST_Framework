from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField
from togo.models import Project, ToDo
from userapp.serializers import UserappModelSerializer


class ProjectSerializer(HyperlinkedModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(HyperlinkedModelSerializer):
    project = ProjectSerializer()
    creator = UserappModelSerializer()

    class Meta:
        model = ToDo
        exclude = ('is_active',)
