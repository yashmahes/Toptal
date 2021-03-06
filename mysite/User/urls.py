from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.UserLogin.as_view()),
    path('register/', views.UserRegister.as_view()),
    path('weather/', views.WeatherData.as_view()),
    path('logout/', views.Logout.as_view()),
]
