from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # optional

    def __str__(self):  # 0 parametros
        """
        Devuelve la representacion de un objeto como una cadena
        """
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=150)
    summary = models.TextField()  # sin límite de longitud
    director_name = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.URLField()  # ImageField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)  # saves the date when the object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # no se puede borrar una categoría, si tiene películas asociadas.

    def __str__(self):  # 0 parametros
        return self.title
