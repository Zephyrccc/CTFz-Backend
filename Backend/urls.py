from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from user.views import UserView, RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from user.views import UserShowDataView

from api.tests import Init

router = DefaultRouter()
router.register('user/profile', UserShowDataView,basename='user/profile')
router.register('user', UserView,basename='user')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('init/', Init.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view()),
    re_path('^', include(router.urls)),
]
