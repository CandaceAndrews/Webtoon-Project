from rest_framework import serializers
from .models import User, Profile

class UserSerializer(serializers.ModelSerializer):
    