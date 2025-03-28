from django.db import models

from django.contrib.auth.models import AbstractUser
from user.managers import UserManager

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    preferences = models.TextField(default='')
    username = models.TextField(null=True, blank=True)

    image = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(default='')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'