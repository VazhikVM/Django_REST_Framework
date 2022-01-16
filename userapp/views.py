from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from userapp.models import UserApp
from userapp.serializers import UserappModelSerializer


class UserappModelViewset(RetrieveModelMixin, UpdateModelMixin, ListModelMixin, GenericViewSet):
    queryset = UserApp.objects.all()
    serializer_class = UserappModelSerializer


