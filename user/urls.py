from django.urls import path
from .views.admin import UserView
from .views.login import LoginHtmlView

app_name = 'user'
urlpatterns = [
    path('login/', LoginHtmlView.as_view()),
]