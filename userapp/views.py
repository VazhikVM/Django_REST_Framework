from rest_framework.viewsets import ModelViewSet
from userapp.models import UserApp
from userapp.serializers import UserappModelSerializer


class UserappModelViewset(ModelViewSet):
    queryset = UserApp.objects.all()
    serializer_class = UserappModelSerializer
