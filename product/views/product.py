from rest_framework import generics
from rest_framework.response import Response
from ..serializers import Category, CategorySerializer
from ..serializers import Product, ProductSerializer
from django.shortcuts import render

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, pk:int):
        product_objs = Product.objects.filter(category = pk)
        product = ProductSerializer(product_objs, many = True)

        category_objs = Category.objects.all()
        categorys = CategorySerializer(category_objs, many = True)

        return render(
            request=request, 
            template_name='category.html', 
            context={'product':product.data}
            )
    
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        product_objs = Product.objects.all()
        product = ProductSerializer(product_objs, many = True)
        return render(
            request=request, 
            template_name='category.html', 
            context={'product':product.data}
            )