# accounts/serializers.py

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from accounts.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
	
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
        	username = validated_data['username'],
        	email = validated_data['email'],
        	password = validated_data['password'],
        )
        Token.objects.create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['is_staff', 'is_superuser']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields =  ['id', 'username', 'email', 'profile']
