from rest_framework import serializers
from .models import User, Weather, Jogging
# class UserRegisterSerializer(serializers.Hyper):
#     pass
class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password', 'email', 'user_type', 'created_at')

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'email')


class WeatherDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = ('location', 'date')

class JoggingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jogging
        fields = ('location', 'date', 'distance', 'start_time', 'end_time')
        