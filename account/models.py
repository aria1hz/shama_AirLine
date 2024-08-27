from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    User_Name =models.CharField(max_length=50)
    email = models.EmailField()
    email_active_code = models.CharField(max_length=100)
    password = models.CharField(max_length=30)