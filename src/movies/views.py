from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse

from django.utils.safestring import mark_safe
from django.views import View
from django.views.generic import ListView

from movies.models import Movie
from movies.templates.forms import MovieForm


def hello_world(request):
    #  name = request.GET["name"]
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world !!")
    else:
        return HttpResponse("Hello " + name)


@login_required
def home(request):
    latest_movies = Movie.objects.all().order_by("-release_date")
    context = {'movies': latest_movies[:4]}
    return render(request, "home.html", context)


@login_required
def movie_detail(request, pk):  # El segundo argumento es el id. de la película
    possible_movies = Movie.objects.filter(pk=pk).select_related("category")  # equivale a un JOIN de SQL
    if len(possible_movies) == 0:
        return render(request, "404.html", status=404)
    else:
        movie = possible_movies[0]
        context = {'movie': movie}
        return render(request, "movie_detail.html", context)


class CreateMovieView(LoginRequiredMixin, View):

    def get(self, request):
        # if request.user.is_autenticated():
        form = MovieForm()
        return render(request, "movie_form.html", {'form': form})

    def post(self, request):
        movie = Movie()
        movie.user = request.user  # asigno a la pelicula el usuario autenticado
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            form = MovieForm()  # formulario vacío
            url = reverse("movie_detail_page", args=[movie.pk])
            message = "Movie created successfully !!"
            # message += mark_safe('<a href="{0}">View</a>'.format(url))
            message += '<a href="{0}">View</a>'.format(url)
            messages.success(request, message)
        return render(request, "movie_form.html", {'form': form})


class MyMoviesView(ListView):  # Ocho métodos asociados a ListView. Se pueden sobreescribir.
    model = Movie
    template_name = "my_movies.html"

    def get_queryset(self):
        queryset = super(MyMoviesView, self).get_queryset()
        return queryset.filter(user=self.request.user)

