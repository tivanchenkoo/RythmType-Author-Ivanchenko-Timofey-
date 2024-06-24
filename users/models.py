from django.db import models
from django.contrib.auth.models import AbstractUser





class Users(AbstractUser):
    users_images = models.ImageField(upload_to='users_profile_images', null=True, blank=True)
    completedLevels = models.CharField(max_length=2000, null=True, blank=True)


    def __str__(self):
        return f"User: {self.username} | ID: {self.id}"
    