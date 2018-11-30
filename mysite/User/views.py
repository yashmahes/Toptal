from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserLoginSerializer, UserRegisterSerializer, WeatherDataSerializer
from .models import User, Weather
from rest_framework.generics import GenericAPIView
import datetime
from rest_framework.response import Response
from rest_framework import status
import logging
from weather import Weather, Unit
import uuid

isAuthenticated = False

class UserRegister(GenericAPIView):
   
    serializer_class = UserRegisterSerializer
    def post(self, request):
        """
        To register user in the system
        ---
        parameters:
                - name: email
                    description: Email of the user
                    required: true
                    type: string
                    paramType: form
                - name: name
                    description: Name of the user
                    required: true
                    type: string
                    paramType: form
                - name: password
                    description: Password
                    required: true
                    type: password
                    paramType: form
                

        responseMessages:
                - code: 400
                    message: Invalid form details
                - code: 500
                    message: Internal server error
                - code: 200
                    message: Success
        """
        try:
            serializer = self.serializer_class(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                data = serializer.data

                return Response({'message': "User successfully registered"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, KeyError, TypeError) as error:
            logging.error(error, exc_info=True)
            content = {'message': "INTERNAL_SERVER_ERROR"}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLogin(GenericAPIView):
   
    serializer_class = UserLoginSerializer
    def post(self, request):
        """
        To login in the system
        ---
        parameters:
                - name: email
                    description: Email of the user
                    required: true
                    type: string
                    paramType: form
                - name: password
                    description: Password
                    required: true
                    type: password
                    paramType: form
               
        responseMessages:
                - code: 400
                    message: Invalid form details
                - code: 401
                    message: Not authenticated
                - code: 422
                    message: Unprocessable request
                - code: 500
                    message: Internal server error
                - code: 200
                    message: Success
        """
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                
                data = serializer.data
                try:
                    user = User.objects.get(email= data['email'])
               
                    if user.password == data['password']:
                        uid = uuid.uuid4()
                        user.access_token = uid.hex
                        user.save()
                        isAuthenticated = True

                        return Response({'message': "User successfully logged in", 'access_token': user.access_token}, status=status.HTTP_200_OK)
                except:
                    return Response("Invalid details", status=status.HTTP_401_UNAUTHORIZED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, KeyError, TypeError) as error:
            logging.error(error, exc_info=True)
            content = {'message': "INTERNAL_SERVER_ERROR"}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class WeatherData(GenericAPIView):
   
    serializer_class = WeatherDataSerializer
    def post(self, request):
        token = request.META.get("Authorizationn")
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
             
                data = serializer.data
                mydate = data['date']
                mylocation = data['location']
                weather = Weather(unit=Unit.CELSIUS)
                location = weather.lookup_by_location(mylocation)
                condition = location.condition
                condition = condition.text

                return Response(condition, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, KeyError, TypeError) as error:
            logging.error(error, exc_info=True)
            content = {'message': "INTERNAL_SERVER_ERROR"}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Logout(GenericAPIView):
   
    serializer_class = UserLoginSerializer
    def get(self, request):
        try:
            isAuthenticated = False
            return Response({'message': "User successfully logged out"}, status=status.HTTP_200_OK)
           
        except (AttributeError, KeyError, TypeError) as error:
            logging.error(error, exc_info=True)
            content = {'message': "INTERNAL_SERVER_ERROR"}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




