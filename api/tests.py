from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from challenge.models import Challenge
User = get_user_model()


class Init(APIView):
    def get(self, request):
        # User.objects.create_superuser(username='admin', password='admin')
        # User.objects.create_user(username='user1', password='user1')
        # User.objects.create_user(username='user2', password='user2')
        # User.objects.create_user(username='user3', password='user3')
        # User.objects.create_user(username='user4', password='user4')
        # User.objects.create_user(username='user5', password='user5')

        Challenge.objects.create(environment_type='docker',title='Challenge1',describe='Challenge1describe',have_attachment=True)
        Challenge.objects.create(environment_type='file',title='Challenge2',describe='Challenge2describe')
        Challenge.objects.create(environment_type='docker',title='Challenge3',describe='Challenge3describe',state=False)
        Challenge.objects.create(environment_type='file',title='Challenge4',describe='Challenge4describe',score=100)
        Challenge.objects.create(environment_type='docker',title='Challenge5',describe='Challenge5describe',have_attachment=True)
        Challenge.objects.create(environment_type='file',title='Challenge6',describe='Challenge6describe')
        return Response("成功")

