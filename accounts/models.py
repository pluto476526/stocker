# accounts/models.py

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Extends the user model
    """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    in_staff = models.BooleanField(default=False)
    in_superusers = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


