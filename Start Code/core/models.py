from django.db import models
from django.contrib.auth.models import AbstractUser


# Register your models here.
class User(AbstractUser):
    pass


class Todo(models.Model):
    description = models.CharField(max_length=255)
