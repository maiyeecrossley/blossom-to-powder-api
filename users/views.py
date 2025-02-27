from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotAuthenticated
from .serializers.common import UserSerializer
from datetime import datetime, timedelta
from django.conf import settings
import jwt

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serialized_user = UserSerializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data, 201)
        return Response(serialized_user.errors, 422)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)

            if not user.check_password(password):
                raise ValidationError("Passwords do not match")
            # generate token:
            exp_date = datetime.now() + timedelta(hours=24)

            token = jwt.encode(
                payload = {
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'is_admin': user.is_staff,
                    },
                    'exp': int(exp_date.strftime('%s'))
                },
                key=settings.SECRET_KEY,
                algorithm='HS256',
            )
            return Response({ 'message': 'Login successful', 'token': token })
        
        except (User.DoesNotExist, ValidationError) as err:
            print(err)
            raise NotAuthenticated("Invalid credentials")