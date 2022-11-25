from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from user.views import RegisterView, LoginView
from challenge.views import ChallengeListView,ChallengeRetrieveView,AttachmentRetrieveView

router = DefaultRouter()
urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('user/', include('user.urls')),
    path('challenge/', include('challenge.urls')),
    re_path('^', include(router.urls)),
]
