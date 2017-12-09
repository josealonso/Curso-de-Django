from django.contrib import admin

from movies.models import Category, Movie

admin.site.register(Category)
admin.site.register(Movie)

