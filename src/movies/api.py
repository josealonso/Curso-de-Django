from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from movies.models import Movie
from movies.serializers import MovieSerializer, MoviesListSerializer


class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return MoviesListSerializer if self.request.method == "GET" else MovieSerializer
        # Esto equivale al operador ternario en JS

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MovieDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
