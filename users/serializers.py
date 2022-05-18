from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "password", "first_name", "second_name", "email", "username", "is_staff", "is_active", ]