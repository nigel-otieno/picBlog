from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
def index(request):
    return render(request, 'picBlogApplication/index.html')

def login(request):
    return render(request, 'picBlogApplication/login.html')

def register(request):
    return render(request, 'picBlogApplication/register.html')

def feed(request):
    return render(request, 'picBlogApplication/feed.html')

def profile(request):
    return render(request, 'picBlogApplication/profile.html')

def profile_edit(request):
    return render(request, 'picBlogApplication/profile_edit.html')

def logout(request):
    request.session.clear()
    return render(request, 'picBlogApplication/index.html')

