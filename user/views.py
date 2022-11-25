
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, LoginSerializer, DataSerializer,SolveInfoSerializer
from .models import User,SolveInfo


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class RegisterView(APIView):
    def post(self, request: Request):
        ser = RegisterSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        refresh = RefreshToken.for_user(user)
        data = dict()
        data['code'] = 201
        data['message'] = '注册成功'
        data['token'] = {'access': str(refresh.access_token), 'refresh': str(refresh)}
        data['result'] = {'id': user.pk, 'username': user.username}
        return Response(data=data, status=status.HTTP_201_CREATED)

class ProfileView(RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = DataSerializer


class SolveInfoView(RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = SolveInfo.objects.all()
    serializer_class = SolveInfoSerializer