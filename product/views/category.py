from rest_framework import generics
from rest_framework.response import Response
from ..serializers import Category, CategorySerializer
from django.shortcuts import render

class ListCreateView(generics.ListCreateAPIView):
    queryset = CategorySerializer
    serializer_class = Category.objects.all()

    def list(self, request):
        category_bojs = Category.objects.all()
        categorys = CategorySerializer(category_bojs, many = True)

        return render(
            request=request, 
            template_name='home.html', 
            context={'category':categorys.data}
            )