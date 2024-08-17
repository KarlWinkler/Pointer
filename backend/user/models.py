from django.db import models

from django.contrib.auth.models import User as AuthUser

class User(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    preferences = models.TextField(default='')

    image = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(default='')

    def __str__(self):
        return f'{self.user.username}'