from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
User = get_user_model()


class Init(APIView):
    def get(self, request):
        User.objects.create_superuser(username='admin', password='admin')
        User.objects.create_user(username='test1', password='test1')
        User.objects.create_user(username='test2', password='test2')
        User.objects.create_user(username='test3', password='test3')
        User.objects.create_user(username='test4', password='test4')
        User.objects.create_user(username='test5', password='test5')
        return Response("成功")
