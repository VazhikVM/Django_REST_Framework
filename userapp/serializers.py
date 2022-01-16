from rest_framework.serializers import HyperlinkedModelSerializer
from userapp.models import UserApp


class UserappModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserApp
        # fields = ('__all__',)
        fields = ('url', 'username', 'first_name', 'last_name', 'email',)
