from rest_framework import serializers
from django.contrib.auth import get_user_model, hashers, password_validation

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError({ 'password_confirmation': 'Passwords do not match' })

        password_validation.validate_password(password)
        data['password'] = hashers.make_password(password)

        return data

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password', 'password_confirmation', 'is_admin')
