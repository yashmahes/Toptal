from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Weather(models.Model):
    location = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.location
   

