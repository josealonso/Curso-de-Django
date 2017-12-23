from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from movies.models import Movie, Category
from movies.permissions import MoviesPermission, CategoriesPermission
from movies.serializers import MovieSerializer, MoviesListSerializer, CategorySerializer


class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "director_name", "category__name", "summary"]
    ordering_fields = ["title", "category", "release_date", "created_at", "modified_at", "rating", "director_name"]

    def get_serializer_class(self):
        return MoviesListSerializer if self.request.method == "GET" else MovieSerializer
        # Esto equivale al operador ternario en JS

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MovieDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [MoviesPermission]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(ModelViewSet):
     queryset = Category.objects.all()
     serializer_class = CategorySerializer
     permission_classes = [CategoriesPermission]