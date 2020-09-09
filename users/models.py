from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customuser(AbstractUser):
    age=models.PositiveIntegerField(default=0,blank=True)
    bio=models.TextField(blank=True)
    photo=models.ImageField(upload_to='user_photos/',blank=True)
    name=models.CharField(max_length=255,blank=True)
    surname=models.CharField(max_length=255,blank=True)