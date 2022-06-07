from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
# from django.contrib.auth.models import User
from authcontroller.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name', 'email', 'roles','is_active')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password = validated_data['password'], first_name=validated_data['first_name'],  last_name=validated_data['last_name'], email=validated_data['email'], roles=validated_data['roles'], is_active=validated_data['is_active'])
        return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'roles', 'is_active')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['roles'] = user.roles
        token['is_active'] = user.is_active
        
        return token

