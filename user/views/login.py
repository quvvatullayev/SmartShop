from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.request import Request
from django.shortcuts import render

class LoginHtmlView(APIView):
    def post(self, request:Request):
        print('hi')
        return render(request=request, template_name='user/login.html', context={'user':{}})

class LoginView(APIView):
    def post(self, request:Request):
        user = request.user
        login(user=user, request=request)
        return Response({})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def custom_logout(request):
    logout(request)
    return Response({'detail': 'Successfully logged out'})
