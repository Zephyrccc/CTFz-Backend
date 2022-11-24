from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from user.views import RegisterView, LoginView, ProfileView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

router = DefaultRouter()
urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('user/profile/<int:pk>', ProfileView.as_view()),
    re_path('^', include(router.urls)),
]
