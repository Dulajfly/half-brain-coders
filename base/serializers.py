from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ExitPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExitPoint
        fields = ['name', 'tracking_difficulty_level', 'wingsuit_difficulty_level', 'rock_drop_second', 'rock_drop_altitude', 'landing_altitude', 'lon', 'lat']


# class UserSerializerWithToken(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#
#         def create(self, validated_data):
#             user = User.objects.create_user(validated_data['username'],
#                                             password = validated_data['password'],
#                                             email = validated_data['email'])
#             return user


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for key, value in serializer.items():
            data[key] = value

        return data