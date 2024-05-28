from django.db import models
from django.utils import timezone

class MusicData(models.Model):
    music_title = models.CharField(max_length=150, null=True, blank=True)
    music_text = models.TextField(null=True, blank=True)
    music_video_links = models.CharField(max_length=1500, null=True, blank=True)
    created_add = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Music title: {self.music_title} | ID: {self.id}'
