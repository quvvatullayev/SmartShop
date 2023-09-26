from rest_framework import generics
from rest_framework.response import Response
from ..serializers import Category, CategorySerializer
from ..serializers import Product, ProductSerializer
from django.shortcuts import render

class ListCreateView(generics.ListCreateAPIView):
    queryset = CategorySerializer
    serializer_class = Category.objects.all()

    def list(self, request):
        category_bojs = Category.objects.all()
        categorys = CategorySerializer(category_bojs, many = True)

        product_objs = Product.objects.all()
        product = ProductSerializer(product_objs, many = True)

        data_boj = Category.objects.first()
        data = CategorySerializer(data_boj).data

        return render(
            request=request,
            template_name='home.html', 
            context={'category':categorys.data, 'product':product.data, 'data':data}
            )