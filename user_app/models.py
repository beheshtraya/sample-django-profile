from django.conf import settings
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthday = models.DateField()

    @property
    def age(self):
        return timezone.now().year - self.birthday.year
