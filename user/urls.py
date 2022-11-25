from django.urls import path
from user.views import SolveInfoView,UserRetrieveView
urlpatterns = [
    path('<int:pk>', UserRetrieveView.as_view()),
    path('solve/info/<int:pk>', SolveInfoView.as_view()),
]
