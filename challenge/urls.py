from django.urls import path
from challenge.views import ChallengeListView, ChallengeRetrieveView, AttachmentRetrieveView
urlpatterns = [
    path('attachment/<int:pk>', AttachmentRetrieveView.as_view()),
    path('<int:pk>', ChallengeRetrieveView.as_view()),
    path('', ChallengeListView.as_view()),
]
