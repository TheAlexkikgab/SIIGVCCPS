from django.shortcuts import render, redirect
from django.contrib.auth import login

# Create your views here.

def home(request):
    return render(request, 'home.html')

# def login(request):
#     return render(request, 'login.html')S