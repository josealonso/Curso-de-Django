from rest_framework import serializers

from movies.models import Movie
from users.serializers import UserSerializer


class MoviesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["id", "title", "image"]


class MovieSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

