from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # optional

class Movie(models.Model):

    title = models.CharField(max_length=150)
    summary = models.TextField()  # sin límite de longitud
    director_name = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.URLField()  # ImageField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)  # saves the date when the object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated
