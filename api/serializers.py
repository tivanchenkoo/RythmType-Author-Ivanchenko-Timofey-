from rest_framework import serializers

from users.models import Users
from music.models import MusicData



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id', 'password', 'last_login', 'username', 'first_name', 'last_name',
            'email', 'users_images'
        )


class MusicDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicData
        fields = (
            'id', 'music_title', 'lyrics', 'music_video_links', 'created_at',
            'music_type', 'music_file', 'song_language', 'intro', 'timings', 'end'
        )