from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

User = get_user_model()

class Authentication(BaseAuthentication):
    def authenticate(self, request):
        if not request.headers:
            return None

        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None

        if not auth_header.startswith("Bearer "):
            raise AuthenticationFailed("Bearer token not valid")

        token = auth_header.replace("Bearer ", "")

        try:
            payload=jwt.decode(
                jwt=token, 
                key=settings.SECRET_KEY, 
                algorithms=['HS256']
            )

            user = User.objects.get(id=payload["user"]["id"])
            return(user, token)

        except Exception as err:
            raise AuthenticationFailed("Invalid credentials")