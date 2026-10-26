from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices

# Create your models here.
class UserRole(TextChoices):
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'User'

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.USER)
    phone_number = models.CharField(max_length=15, unique=True)