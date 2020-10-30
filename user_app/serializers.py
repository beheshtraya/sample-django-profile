from django.contrib.auth.models import User
from rest_framework import serializers

from user_app.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    age = serializers.IntegerField()

    class Meta:
        model = Profile
        fields = '__all__'
