from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, UserDataSerializer
from .models import User
from django.contrib.auth import get_user_model, authenticate, login


class LoginView(APIView):
    def post(self, request: Request):
        ser = LoginSerializer(data=request.data)
        if ser.is_valid():
            username = ser.validated_data['username']
            password = ser.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if not user:
                data = dict()
                data['status'] = 400
                data['message'] = '账号或密码错误'
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
            else:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                data = dict()
                data['status'] = 200
                data['message'] = '登录成功'
                data['token'] = {'access': str(refresh.access_token), 'refresh': str(refresh)}
                data['result'] = {'id': user.pk, 'username': user.username}
                return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = dict()
            data['status'] = 400
            data['message'] = '参数错误'
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request: Request):
        ser = RegisterSerializer(data=request.data)
        if ser.is_valid():
            username = ser.validated_data['username']
            password = ser.validated_data['password']
            User = get_user_model()
            user = User.objects.create_user(
                username=username, password=password)
            refresh = RefreshToken.for_user(user)
            data = dict()
            data['status'] = 201
            data['message'] = '注册成功'
            data['token'] = {'access': str(refresh.access_token), 'refresh': str(refresh)}
            data['result'] = {'id': user.pk, 'username': user.username}
            data['result'] = {'id': user.pk, 'username': user.username}
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            data = dict()
            data['status'] = 400
            data['message'] = '参数错误'
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserDataSerializer
