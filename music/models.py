from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

import os


def validate_file_size(file):
    max_size_kb = 6000  # 6 MB
    if file.size > max_size_kb * 1024:
        raise ValidationError(f"Maximum file size {max_size_kb} kb")
    

def validate_mp3_file(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.mp3']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only MP3 files are allowed.')    

 

class MusicData(models.Model):
    music_type = models.CharField(max_length=15, null=True, blank=True)
    music_title = models.CharField(max_length=150, null=True, blank=True)
    musician_performer = models.CharField(max_length=150, null=True, blank=True)
    artists_social_networks = models.CharField(max_length=300, null=True, blank=True)
    lyrics = models.TextField(null=True, blank=True)
    music_video_links = models.CharField(max_length=1500, null=True, blank=True)
    song_language = models.CharField(max_length=5, null=True, blank=True)
    intro = models.IntegerField(null=True, blank=True)
    timings = models.CharField(max_length=1000, null=True, blank=True)
    end = models.IntegerField(null=True, blank=True)

    music_file = models.FileField(
        upload_to='music_file', max_length=80, validators=(validate_file_size, validate_mp3_file, ), 
        null=True, blank=True, unique=True
        )
    
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Musican {self.musician_performer} | Music title: {self.music_title} | ID: {self.id}'
