from rest_framework import serializers
from django.contrib.auth import get_user_model, hashers, password_validation

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data['password']
        password_validation.validate_password(password)
        data['password'] = hashers.make_password(password)

        return data

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password', 'is_admin')
