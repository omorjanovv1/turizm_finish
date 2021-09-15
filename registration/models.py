from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(
        verbose_name='First name',
        max_length=100, null=True, blank=True
    )
    last_name = models.CharField(
        verbose_name='Last name',
        max_length=100, null=True, blank=True
    )


    def __str__(self):
        return f"{self.username}--{self.id}"
