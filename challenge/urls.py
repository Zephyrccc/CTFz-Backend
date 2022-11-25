from django.urls import path
from challenge.views import ChallengeListView, ChallengeRetrieveView,TagListView,CategoryListView
urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('tag/', TagListView.as_view()),
    path('<int:pk>', ChallengeRetrieveView.as_view()),
    path('', ChallengeListView.as_view()),
]
