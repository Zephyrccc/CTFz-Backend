from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import (LoginView, RegisterView, UserListView, UserRetrieveView,
                    TeamListView, TeamRetrieveView, TagListView, CategoryListView,
                    ChallengeListView, ChallengeRetrieveView,SolveInfoListView,
                    JoinRequestListView)
urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('team/<int:pk>', TeamRetrieveView.as_view()),
    path('team/', TeamListView.as_view()),
    path('user/<int:pk>', UserRetrieveView.as_view()),
    path('user/', UserListView.as_view()),
    path('tag/', TagListView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('challenge/<int:pk>', ChallengeRetrieveView.as_view()),
    path('challenge/', ChallengeListView.as_view()),
    path('solve/info/', SolveInfoListView.as_view()),
    path('join/request/', JoinRequestListView.as_view()),
]
