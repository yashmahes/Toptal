import logging
from functools import wraps
from django.conf import settings
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status

from User.models import User, Weather

CACHE_TIMEOUT = settings.CACHE_TIMEOUT
logging.getLogger(__name__)

def requires_auth(function):

    @wraps(function)
    def wrapper(request, *args, **kwargs):
        token = args[0].META.get('HTTP_AUTHORIZATION')
        try:
            token_array = token.split(' ')

            if token_array[0] != 'bearer':
                logging.warning(args[0].META.get('PATH_INFO'))
                logging.warning('----Logged out because token was not in right format----')
                return Response({'message': "ACCESS_TOKEN_EXPIRED"}, status=status.HTTP_401_UNAUTHORIZED)

            try:
                users = User.objects.get(access_token= token_array[1])
            except:
                return Response({'message': "ACCESS_TOKEN_EXPIRED"}, status=status.HTTP_401_UNAUTHORIZED)
        
            rsa_public_key = cache.get(users.email)

        except (AttributeError, KeyError, TypeError) as error:
            logging.warning(args[0].META.get('PATH_INFO'))
            logging.error(error, exc_info=True)
            return Response({'message': "ACCESS_TOKEN_EXPIRED"}, status=status.HTTP_401_UNAUTHORIZED)

        return function(request, *args, **kwargs)

    return wrapper


