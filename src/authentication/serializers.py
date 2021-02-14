from rest_framework import serializers
from .models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=5, max_length=20, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    def validate(self, attrs):
        """
        Validates user attributes
        """
        email = attrs.get("email")

        if email is None:
            raise serializers.ValidationError("The email is required")
        return attrs

    def create(self, validated_data):
        """
        Creates user
        """
        return CustomUser.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=5, max_length=20, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    def validate(self, attrs):
        """
        Validates user attributes
        """
        email = attrs.get("email")
        password = attrs.get("pasword")

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise serializers.AuthenticationFailed("The user does not exist")

        return {"email": user.email}
