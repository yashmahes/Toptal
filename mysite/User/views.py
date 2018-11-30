from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserLoginSerializer, UserRegisterSerializer
from .models import User



