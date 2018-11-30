from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserLoginSerializer, UserRegisterSerializer
from .models import User
from rest_framework.generics import GenericAPIView
import datetime
from rest_framework.response import Response
from rest_framework import status
import logging


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
                - name: phone_no
                    description: Phone number of the user
                    required: true
                    type: string
                    paramType: form
                - name: country_code
                    description: Country Code of the user
                    required: true
                    type: string
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


