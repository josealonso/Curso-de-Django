from django.forms import ModelForm

from movies.models import Movie


class MovieForm(ModelForm):

    class Meta:
        model = Movie
        # fields = '__all__'
        exclude = ["user"]  # no muestra ese campo en el formulario
