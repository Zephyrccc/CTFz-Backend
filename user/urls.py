from django.urls import path
from user.views import SolveInfoListView,UserRetrieveView
urlpatterns = [
    path('<int:pk>', UserRetrieveView.as_view()),
    path('solve/info/', SolveInfoListView.as_view()),
]
