from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    class Meta:
        db_table = "users"
