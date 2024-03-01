from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


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

    def post(self, request, *args, **kwargs):
        '''Сразу активация пользователя is_active = True'''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user = serializer.instance
        user.is_active = True
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
