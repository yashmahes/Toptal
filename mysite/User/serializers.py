from rest_framework import serializers
from .models import User, Weather
# class UserRegisterSerializer(serializers.Hyper):
#     pass
class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password', 'email', 'user_type')

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'email')


class WeatherDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = ('location', 'date')


        