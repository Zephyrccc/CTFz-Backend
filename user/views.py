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
from user.serializers import UserSerializer, LoginAndRegisterSerializer

User = get_user_model()


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class LoginView(TokenObtainPairView):
#     serializer_class = CustomObtainPairSerializer


class RegisterView(APIView):
    def post(self, request: Request):
        ser = LoginAndRegisterSerializer(data=request.data)
        if ser.is_valid():
            username = ser.validated_data['username']
            user = User.objects.filter(username=username)
            if not user:
                password = ser.validated_data['password']
                user = User.objects.create_user(username=username, password=password)
                return Response({"code": '200', 'msg': 'register success'})
        else:
            return Response({'status': False, 'message': '格式错误'})


# class RegisterView(APIView):
#     def post(self, request: Request):
#         ser = LoginAndRegisterSerializer(data=request.data)
#         ser.is_valid(raise_exception=True)
#         username = ser.validated_data['username']
#         password = ser.validated_data['password']
#         user = User.objects.create_user(username=username, password=password)
#         return Response({"code": '200', 'msg': 'register success'})