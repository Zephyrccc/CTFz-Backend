from rest_framework import mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from user.serializers import UserRegSerializer

User = get_user_model()


class UserRegViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer