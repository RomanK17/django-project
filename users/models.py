from django.db import models
from django.contrib.auth.models import AbstractUser # как посмотреть какие поля есть у AbstractUser?
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True) # поле может быть пустым + необязательное