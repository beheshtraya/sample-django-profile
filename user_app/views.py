from rest_framework.viewsets import ModelViewSet

from user_app.filters import ProfileFilter
from user_app.models import Profile
from user_app.serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all().order_by('-birthday')
    serializer_class = ProfileSerializer
    filter_class = ProfileFilter
