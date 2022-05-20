from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password



class UserRegistrationSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_password(password: str) -> str:
        return make_password(password)

    class Meta:
        model = User
        fields = ['email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    class Meta:
        model = User
        fields = ['email','password']
