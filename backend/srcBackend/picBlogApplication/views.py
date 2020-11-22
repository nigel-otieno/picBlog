from django.shortcuts import render, redirect
from .models import *

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

