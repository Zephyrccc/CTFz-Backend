from rest_framework import serializers
from .models import Challenge,Tag,Category


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id','environment_type', 'category', 'title', 'describe', 'score','have_attachment', 'mark_total', 'mark_count', 'category', 'tag', 'attachment']
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

