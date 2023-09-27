from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from ..serializers import UserSerializers
from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer
from django.shortcuts import render

class UserView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request:Request):
        product_objs = Product.objects.all()
        products = ProductSerializer(product_objs, many = True)

        categorys_objs = Category.objects.all()
        categorys = CategorySerializer(categorys_objs, many = True)

        return render(
            request=request,
            template_name='user/admin.html',
            context={
                'products':products.data,
                'category':categorys.data
                }
        )