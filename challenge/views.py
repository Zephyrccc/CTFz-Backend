from rest_framework.generics import RetrieveAPIView,ListAPIView
from .models import Challenge,Attachment
from .serializers import ChallengeSerializer,AttachmentSerializer

class ChallengeListView(ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class ChallengeRetrieveView(RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class AttachmentRetrieveView(RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
