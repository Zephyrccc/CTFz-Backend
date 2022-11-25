from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User,Profile

# 登录信息序列化
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        super().validate(attrs)
        refresh = self.get_token(self.user)
        token = {'access': str(refresh.access_token), 'refresh': str(refresh)}
        result = {'id': self.user.pk, 'username': self.user.username}
        return {'code': 200, 'message': '登录成功', 'token': token, 'result': result}


class RegisterSerializer(serializers.ModelSerializer):
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


# 用户资料部分
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id', 'user']


# 展示用户所有信息
class DataSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'profile']
