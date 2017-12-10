from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from movies.models import Movie


def hello_world(request):
    #  name = request.GET["name"]
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world !!")
    else:
        return HttpResponse("Hello " + name)


def home(request):
    latest_movies = Movie.objects.all().order_by("-release_date")
    context = {'movies': latest_movies[:4]}
    return render(request, "home.html", context)


def movie_detail(request, pk):  # El segundo argumento es el id. de la película
    possible_movies = Movie.objects.filter(pk=pk).select_related("category")  # equivale a un JOIN de SQL
    if len(possible_movies) == 0:
        return render(request, "404.html", status=404)
    else:
        movie = possible_movies[0]
        context = {'movie': movie}
        return render(request, "movie_detail.html", context)


