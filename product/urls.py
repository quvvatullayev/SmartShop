from django.urls import path
from .views.category import ListCreateView
from .views.product import ProductListCreateView

app_name = 'product'
urlpatterns = [
    path('', ListCreateView.as_view(), name = 'categorys'),
    path('category/product/<int:pk>/', ProductListCreateView.as_view(), name='category_by_product')
]