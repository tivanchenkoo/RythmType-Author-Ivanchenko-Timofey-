from django.urls import path, include, re_path
from rest_framework import routers

from api import views


app_name = 'api'

router = routers.SimpleRouter()
router.register(r'users_list', views.UsersViewSet)
router.register(r'music_data_list', views.MusicDataViewSet)



urlpatterns = [
    path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/rythm_type/api/v1/users_list/
    path('api/v1/auth/', include('djoser.urls')), #127.0.0.1:8000/api/v1/auth/ что-бы получить ссылку на токен
    re_path(r'auth/', include('djoser.urls.authtoken')), #127.0.0.1:8000/api/v1/auth/....
]