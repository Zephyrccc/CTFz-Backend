from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, SolveInfo


class LoginSerializer(TokenObtainPairSerializer):
    """
    登录序列化
    """

    def validate(self, attrs):
        super().validate(attrs)
        refresh = self.get_token(self.user)
        token = {'access': str(refresh.access_token), 'refresh': str(refresh)}
        result = {'id': self.user.pk, 'username': self.user.username}
        return {'code': 200, 'message': '登录成功', 'token': token, 'result': result}


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
    """
    用户模型序列化
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'sex', 'solve_info']
        extra_kwargs = {"password": {"write_only": True}}

    def update(self, instance, validated_data):
        result_instance = super().update(instance, validated_data)
        password = validated_data.get('password', None)
        if not password:
            pass
        else:
            result_instance.set_password(validated_data['password'])
            result_instance.save()
        return result_instance


class SolveInfoSerializer(serializers.ModelSerializer):
    """
    解题信息序列化
    """
    class Meta:
        model = SolveInfo
        exclude = ['id', 'user']
