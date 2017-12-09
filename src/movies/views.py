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
