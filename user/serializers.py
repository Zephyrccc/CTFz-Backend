from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models

# 登录信息序列化
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


# 注册信息序列化
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
# 单独改密码
# user.set_password(validated_data['password'])
# user.save()


# 账户信息序列化
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password']


# 用户资料部分
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        exclude = ['id', 'user']


# 展示用户所有信息
class UserShowDataSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(many=False)

    class Meta:
        model = models.User
        fields = ['id', 'username', 'profile']
