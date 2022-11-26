from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, SolveInfoSerializer, UserDateSerializer
from .models import User, SolveInfo
from .permissions import IsOwner


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
        data['access'] = str(refresh.access_token)
        data['refresh'] = str(refresh)
        data['result'] = {'id': user.pk, 'username': user.username}
        return Response(data=data, status=status.HTTP_201_CREATED)

# @permission_classes([IsAuthenticated(),IsOwner()])


class UserRetrieveView(RetrieveAPIView, UpdateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        return UserDateSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsOwner(), ]


class SolveInfoView(RetrieveAPIView):
    queryset = SolveInfo.objects.all()
    serializer_class = SolveInfoSerializer
