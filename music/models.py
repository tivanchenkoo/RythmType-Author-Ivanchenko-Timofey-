from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError




def validate_file_size(file):
    max_size_kb = 6000  # 6 MB
    if file.size > max_size_kb * 1024:
        raise ValidationError(f"Maximum file size {max_size_kb} kb")

 

class MusicData(models.Model):
    music_type = models.CharField(max_length=15, null=True, blank=True)
    music_title = models.CharField(max_length=150, null=True, blank=True)
    music_text = models.TextField(null=True, blank=True)
    music_video_links = models.CharField(max_length=1500, null=True, blank=True)

    music_file = models.FileField(
        upload_to='music_file', max_length=50, validators=(validate_file_size, ), 
        null=True, blank=True, unique=True
        )
    
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Music title: {self.music_title} | ID: {self.id}'
