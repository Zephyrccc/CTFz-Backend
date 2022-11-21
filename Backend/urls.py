from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from user.views import UserView, RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('user', UserView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view()),
    re_path('^', include(router.urls)),
]
