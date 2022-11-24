from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from user.views import RegisterView, LoginView, UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from api.tests import Init

router = DefaultRouter()
urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('user/profile/<int:pk>', UserProfileView.as_view()),
    path('init', Init.as_view()),
    re_path('^', include(router.urls)),
]
