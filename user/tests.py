
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import get_user_model
from user.serializers import LoginSerializer
from datetime import datetime

User = get_user_model()


# class LoginView(APIView):
#     def post(self, request: Request):
#         ser = LoginSerializer(data=request.data)
#         if ser.is_valid():
#             username = ser.validated_data.get('username')
#             user = User.objects.filter(username=username).first()
#             if user:
#                 rest = check_password(pwd, user.password)
#                 ser.save(last_login=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#                 return Response({'status': True, 'message': '注册成功', 'result': {'id': ser.instance.id, 'username': ser.instance.username}})

#         user_name = request.data.get("username")
#         print(user_name)
#         pwd = request.data.get("password")
#         phone = request.data.get("phone")
#         code = request.data.get('code')
#         print(code)
#         # 校验短信验证码
#         client = redis.Redis()
#         # msmcode = 'code_%s' % phone
#         # msmcodes = client.get(msmcode)
#         msmcodes = client.get('sms_%s' % phone).decode()
#         print('>>>>>>>>>>>>>>>', msmcodes)
#         # 校验验证码是否过期
#         if not msmcodes:
#             return Response({'msg': '验证码过期请重新登陆', "code": '204'})
#         # 校验验证码是否正确
#         if msmcodes != code:
#             return Response({'msg': '验证码错误请重新输入', "code": '401'})
#         # 登录
#         user = User.objects.get(username=user_name)
#         user.last_login = time.strftime('%Y-%m-%d %H:%M:%S')
#         user.save()
#         # 密码效验
#         rest = check_password(pwd, user.password)
#         #
#         if not rest:
#             return Response({'msg': '密码错误', "code": '204'})
#         # 加密时生成第二部分的字符串
#         payload_dict = jwt_payload_handler(user)
#         # 生成token
#         token = jwt_encode_handler(payload_dict)
#         resource_list = get_resource_list(user)
#         return Response({'msg': 'login success', 'token': token, "code": '200', 'resource_list': resource_list})


class RegisterView(APIView):
    def post(self, request: Request):
        ser = LoginSerializer(data=request.data)
        if not ser.is_valid():
            return
        user = User.objects.filter(username=ser.validated_data['username'])
        if user:
            return Response({'code': 502, 'msg': '用户名重复'})
        username = ser.validated_data['username']
        password = ser.validated_data['password']
        user = User.objects.create_user(username=username, password=password)
        return Response({"code": '200', 'msg': 'register success'})
