from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# métodos past y put


class MovieDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

