from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Team, Tag, Category, Challenge, SolveInfo,JoinRequest


class LoginSerializer(TokenObtainPairSerializer):
    """
    登录序列化
    """

    def validate(self, attrs):
        super().validate(attrs)
        refresh = self.get_token(self.user)
        return {'code': 200, 'access': str(refresh.access_token), 'refresh': str(refresh), 'id': self.user.pk}


class RegisterSerializer(serializers.ModelSerializer):
    """
    注册序列化
    """
    class Meta:
        model = User
        fields = ['username', 'password']
    extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user

# 单独改密码
# user.set_password(validated_data['password'])
# user.save()


class UserSerializer(serializers.ModelSerializer):
    solve_info = serializers.SerializerMethodField(
        method_name='getSloveInfoList', read_only=True)

    def getSloveInfoList(self, user):
        solve_info_list = []
        for solve_info in user.solve_info.all():
            solve_info_list.append({'id': solve_info.pk, "title": solve_info.title,
                                   "category": solve_info.category.name, "score": solve_info.score})
        return solve_info_list

    class Meta:
        model = User
        fields = ['id', 'username', 'sex', 'solve_info',
                  'describe', 'total_score', 'team']
        depth = 1
        extra_kwargs = {
            'password': {'write_only': True}
        }


class TeamSerializer(serializers.ModelSerializer):

    captain = serializers.SerializerMethodField(
        method_name='getUserInfo', read_only=True)
    member = serializers.SerializerMethodField(
        method_name='getUserInfoList', read_only=True)

    def getUserInfo(self, team):
        return {'id': team.captain.pk, "username": team.captain.username, "sex": team.captain.sex, "describe": team.captain.describe, "total_score": team.captain.total_score, "team": team.captain.team.pk}

    def getUserInfoList(self, team):
        member_list = []
        for member in team.member.all():
            member_list.append({'id': member.pk, "username": member.username, "sex": member.sex,"solve_info":member.solve_info.count(),
                               "describe": member.describe, "total_score": member.total_score, "team": member.team.pk})
        return member_list

    class Meta:
        model = Team
        fields = ['id', 'name', 'captain', 'declare',
                  'describe', 'member', 'created_time']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'environment_type', 'category', 'tag',
                  'describe', 'score', 'difficulty', 'attachment', 'created_time']
        depth = 1


class SolveInfoSerializer(serializers.ModelSerializer):
    """
    解题信息序列化
    """

    user = serializers.SerializerMethodField(
        method_name='getUserInfo', read_only=True)
    challenge = serializers.SerializerMethodField(
        method_name='getChallengeInfo', read_only=True)

    def getUserInfo(self, solve_info):
        return {'id': solve_info.user.pk, "username": solve_info.user.username}

    def getChallengeInfo(self, solve_info):
        return {'id': solve_info.challenge.pk, "title": solve_info.challenge.title, 'category': solve_info.challenge.category.name}

    class Meta:
        model = SolveInfo
        exclude = ['id']
        # fields = '__all__'


class JoinRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRequest
        # fields = ['user', 'team', 'state', 'time']
        fields = '__all__'