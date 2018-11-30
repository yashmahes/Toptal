from rest_framework import serializers
from .models import User
# class UserRegisterSerializer(serializers.Hyper):
#     pass
class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password', 'email', 'role')

class UserLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'email')


