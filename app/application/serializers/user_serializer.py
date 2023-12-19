from application.serializers.base_serializer import BaseSerializer
from domain.entities.user_entity import UserEntity
from rest_framework import serializers


class UserSerializer(BaseSerializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200, write_only=True)
    email = serializers.EmailField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    is_active = serializers.BooleanField(required=False, default=True)

    def to_entity(self):
        return UserEntity(
            username=self.validated_data["username"],
            password=self.validated_data["password"],
            email=self.validated_data["email"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            is_active=self.validated_data["is_active"],
        )
