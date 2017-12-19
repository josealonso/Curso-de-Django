from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UsersListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name =serializers.CharField()
    last_name = serializers.CharField()


class UserSerializer(UsersListSerializer):
    # Actúa como un traductor de objetos a tipos primitivos
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_username(self, data):
        if self.instance is None and User.objects.filter(username=data).exists():
            # La primera condiC se cumple c- se está creando un usuario
            raise ValidationError("User already exists")
        if self.instance and self.instance.username != data and User.objects.filter(username=data).exists():
            # La primera condiC se cumple c- se está actualizando un usuario
            raise ValidationError("Wanted username already in use")
        return data

    def create(self, validated_data): # Construye un objeto User
        instance = User()  # Actúa como un formulario
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.set_password(validated_data.get("password"))
        # El método "set_password" cifra la contraseña
        # instance.password = validated_data.get("password")
        instance.save()

