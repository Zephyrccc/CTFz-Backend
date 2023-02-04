from rest_framework.generics import RetrieveAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Challenge, Tag, Category
from .serializers import ChallengeSerializer, TagSerializer, CategorySerializer


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
