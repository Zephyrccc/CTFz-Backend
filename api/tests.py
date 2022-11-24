from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from challenge.models import Challenge
User = get_user_model()


class Init(APIView):
    def get(self, request):
        User.objects.create_user(username='user1', password='user1')
        User.objects.create_user(username='user2', password='user2')
        User.objects.create_user(username='user3', password='user3')
        User.objects.create_user(username='user4', password='user4')
        User.objects.create_user(username='user5', password='user5')
        return Response("成功")

