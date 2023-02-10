from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Team, Tag, Category, Challenge,SolveInfo,JoinRequest
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer, TeamSerializer, TagSerializer, CategorySerializer, ChallengeSerializer,SolveInfoSerializer,JoinRequestSerializer
# Create your views here.


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
        data['access'] = str(refresh.access_token)
        data['refresh'] = str(refresh)
        data['id'] = user.pk
        return Response(data=data, status=status.HTTP_201_CREATED)

# @permission_classes([IsAuthenticated(),IsOwner()])


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return UserSerializer
    #     return UserDateSerializer

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [IsAuthenticated()]
    #     return [IsAuthenticated(), IsOwner(), ]


class TeamListView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamRetrieveView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ChallengeListView(ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category', 'tag']


class ChallengeRetrieveView(RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SolveInfoListView(ListAPIView):
    queryset = SolveInfo.objects.all()
    serializer_class = SolveInfoSerializer


class JoinRequestListView(ListAPIView):
    queryset = JoinRequest.objects.all()
    serializer_class = JoinRequestSerializer