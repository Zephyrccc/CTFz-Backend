from rest_framework import serializers
from .models import Challenge, Tag, Category


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'category', 'title', 'describe', 'score', 'difficulty','tag', 'environment_type', 'have_attachment',  'attachment','created_time']
        # depth = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
