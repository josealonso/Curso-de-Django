from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from users.serializers import UserSerializer, UsersListSerializer


class HelloWorld(APIView):

    def get(self, request):
        return Response(['hello', 'world'])

    def post(self, request):
        return Response(request.data)

    def put(self, request):
        return Response(request.data)


class UsersListAPI(APIView):


    def get(self, request):
        users = User.objects.all()  # users es un objeto q hay q convertir al formato de salida
        serializer = UsersListSerializer(users, many=True)  # muchos usuarios
        #  El serializador obtiene un diccionario por cada usuario de la lista
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  #  Llama a create o a update
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        # Llama al método create de serializers.py
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        # Llama al método update de serializers.py
        if serializer.is_valid:
            user = serializer.save()
            return  Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Según REST, put no es lo mismo que patch, pues en este último se actualiza
        # solo un campo ---> campo "partial" del serializador igual a True

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
