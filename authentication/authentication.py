from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

User = get_user_model()

class JWTAuthentication(BasicAuthentication):
    def authenticate(self, request):
        header = request.headers.get('Authorization')
        print('header received:', header)

        if not header:
            return None

        if not header.startswith('Bearer '):
            raise PermissionDenied(detail='Invalid Auth token')

        token = header.replace('Bearer ', '')
        print("token:", token)

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            print("PAYLOAD:", payload)  
            user = User.objects.get(pk=payload.get('sub'))
        except jwt.ExpiredSignatureError as e:
            print("EXPIRED TOKEN:", e)
            raise PermissionDenied(detail='Token expired')
        except jwt.exceptions.InvalidTokenError as e:
            print("TOKEN DECODE ERROR:", e)
            raise PermissionDenied(detail='Invalid Token')
        except User.DoesNotExist:
            raise PermissionDenied(detail='User Not Found')

        return (user, token)

