from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	username = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=100, unique=True)
	is_admin = models.BooleanField(default=False)
	
	
