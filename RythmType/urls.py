from django.contrib import admin
from django.urls import path, include, re_path
from django.conf  import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rythm_type/', include('api.urls')),

    #http://127.0.0.1:8000/rythm_type/api/v1/session/auth/login/
    #http://127.0.0.1:8000/rythm_type/api/v1/session/auth/logout/ #при логоут нужно редирект настроить 
    path('api/v1/session/auth/', include('rest_framework.urls', namespace='rest_framework')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)