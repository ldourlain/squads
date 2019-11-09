from django.db import models
from django.contrib.auth.models import AbstractUser


class Administrator(AbstractUser):
    # to do: classrooms
    # classrooms = models.ManyToManyField()
    def __str__(self):
        return self.username
