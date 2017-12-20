from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MoviesListAPI(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)