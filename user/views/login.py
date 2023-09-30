from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.request import Request
from django.shortcuts import render
from product.serializers import Category, CategorySerializer

class LoginHtmlView(APIView):
    def get(self, request:Request):
        user = request.user
        print('hi')
        category_objs = Category.objects.all()
        categorys = CategorySerializer(category_objs, many = True)

        return render(
            request=request, 
            template_name='user/login.html', 
            context={
                'category':categorys.data
                }
            )