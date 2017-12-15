from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.Serializer):
    # Actúa como un traductor de objetos a tipos primitivos
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_username(self, data):
        if User.objects.filter(username=data).exists():
            raise ValidationError("User already exists")
        return data

    def create(self, validated_data): # Construye un objeto User
        instance = User()  # Actúa como un formulario
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.set_password(validated_data.get("password"))
        # El método "set_password" cifra la contraseña
        # instance.password = validated_data.get("password")
        instance.save()
        return instance

    def update(self, instance, validated_data):
        pass
