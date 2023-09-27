from django.urls import path
from .views.login import LoginView
from .views.admin import UserView

app_name = 'user'
urlpatterns = [
    path('login/', LoginView.as_view()),
    path('adminview/', UserView.as_view(), name = 'adminview'),
]