from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth.models import User
from ..serializers import UserSerializers
from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request:Request):

        return render(request=request, template_name='user/login.html', context={})
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def create(self, request:Request, *args, **kwargs):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(id = serializer.data['id'])
            token = Token.objects.create(user = user)
            return Response({'token':token.key})
        return Response({"errors":serializer.errors})