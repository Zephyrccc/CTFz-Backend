from rest_framework import serializers
from .models import Challenge, Attachment


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        exclude = ['id', 'state', 'is_fixed_flag', 'flag', 'created_time']


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        exclude = ['challenge_one']
