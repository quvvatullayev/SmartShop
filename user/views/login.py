from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import render

class LoginView(APIView):
    def get(self, request:Request):
        return render(request=request, template_name='user/login.html', context={})