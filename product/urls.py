from django.urls import path
from .views.category import ListCreateView

app_name = 'product'
urlpatterns = [
    path('', ListCreateView.as_view(), name = 'categorys')
]