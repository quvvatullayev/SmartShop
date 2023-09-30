from django.urls import path
from .views.admin import UserView
from .views.login import LoginView, custom_logout, LoginHtmlView

app_name = 'user'
urlpatterns = [
    path('custom_login/', LoginView.as_view(), name='custom_login'),
    path('login/', LoginHtmlView.as_view()),
    path('logout/',custom_logout, name='custom_logout'),
]