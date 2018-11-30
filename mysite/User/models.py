from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    accesstoken = models.CharField(max_length=255)
    

class Weather(models.Model):
    location = models.CharField(max_length=50)
    date = models.DateField()
   

