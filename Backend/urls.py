from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from user.views import RegisterView, LoginView,UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from api.tests import Init


router = DefaultRouter()


from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="接口文档",
        default_version='v1',
        description="Welcome to the world of Tweet",
        terms_of_service="https://www.tweet.org",
        contact=openapi.Contact(email="demo@tweet.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # swagger
    re_path(r'^doc(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('admin/', admin.site.urls),
    path('init/', Init.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view()),
    path('user/profile/<int:pk>', UserProfileView.as_view()),
    re_path('^', include(router.urls)),
]
