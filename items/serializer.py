from rest_framework import serializers
from .models import Items
from django.contrib.auth.models import User
import re

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = "__all__"

    def validate_username(self, value):
        if re.search(r'\d', value):
            raise serializers.ValidationError("Username should not contain numbers.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Items
        fields = ['item_name', 'item_description']
