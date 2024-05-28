from django.db import models
from django.contrib.auth.models import AbstractUser





class Users(AbstractUser):
    users_images = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return f"User: {self.username} | ID: {self.id}"
    