from user.serializers import CustomObtainPairSerializer
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import get_user_model
from user.serializers import UserRegSerializer

User = get_user_model()



class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer


class LoginView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer


class RegView(CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        ret_dict = serializer.data
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        ret_dict["token"] = access_token
        headers = self.get_success_headers(serializer.data)
        return Response(ret_dict, status=status.HTTP_201_CREATED, headers=headers)
