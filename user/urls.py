from django.urls import path
from user.views import ProfileView,SolveInfoView
urlpatterns = [
    path('user/profile/<int:pk>', ProfileView.as_view()),
    path('solve/info/<int:pk>', SolveInfoView.as_view()),
]
