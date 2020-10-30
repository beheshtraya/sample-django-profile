from rest_framework import routers
from . import views

router = routers.SimpleRouter(trailing_slash=False)

router.register('profiles', views.ProfileViewSet, basename='profile')
