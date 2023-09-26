from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4



class Account(AbstractUser):
    id = models.UUIDField( primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)
    

