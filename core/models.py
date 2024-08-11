from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    balance = models.PositiveIntegerField(default=0)

