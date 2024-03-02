from rest_framework import generics, status
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        '''Сохранение пароля'''
        user = serializer.save()
        password = self.request.data.get('password')
        user.set_password(password)
        user.save()
