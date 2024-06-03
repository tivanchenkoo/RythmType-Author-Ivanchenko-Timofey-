from django.urls import path, include
from rest_framework import routers

from api import views


app_name = 'api'

router = routers.SimpleRouter()
router.register(r'users_list', views.UsersViewSet)
router.register(r'music_data_list', views.MusicDataViewSet)



urlpatterns = [
    #http://127.0.0.1:8000/rythm_type/api/v1/users_list/
    path('api/v1/', include(router.urls)), 

]