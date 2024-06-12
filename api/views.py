from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.models import Users
from music.models import MusicData

from api.serializers import UsersSerializer, MusicDataSerializer
from api.permissions import IsAdminOrReadOnly, IsAdminOrOwner



class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAdminOrOwner, )


    # Only admin has all permissions to (GET, POST, PATCH, DELETE) or read ALL data!
    # Each authorized user only has access to personal information and can change it use (GET, POST, PUT, DELETE)
    def get_queryset(self):
        if self.request.user.is_staff:           
            return Users.objects.all()
        elif self.request.user.is_authenticated or self.request.user.is_staff:
            user_id = self.request.user.id
        return Users.objects.filter(pk=user_id)
    



class MusicDataViewSet(ModelViewSet):
    queryset = MusicData.objects.all()
    serializer_class = MusicDataSerializer
    permission_classes = (IsAdminOrReadOnly, )

