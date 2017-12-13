from django.contrib import admin
from django.utils.safestring import mark_safe

from movies.models import Category, Movie

admin.site.register(Category)
# admin.site.register(Movie)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'rating', 'user_full_name', 'category')
    list_filter = ('category', 'director_name', 'summary')
    search_fields = ('title', 'director_name', 'summary')

    def user_full_name(self, movie):
        return "{0} {1}".format(movie.user.first_name, movie.user.last_name)

    user_full_name.short_description = "Movie owner"  # Añado un atributo al método
    user_full_name.admin_order_field = "user__first_name"

    def get_image_html(self, movie):
        return mark_safe('<img src="{0}" alt="{1}" height="100">'.format(movie.image, movie.title))
    get_image_html.short_description = "Movie poster"

    readonly_fields = ('created_at', 'modified_at', 'get_image_html')   # Nuevo en Django 2
    # Los campos personalizados deben ser de solo lectura
    fieldsets = (
        (None, {
            'fields': ('title', 'summary')
        }),  # Las tuplas de un solo elemento deben llevar una coma
        ("Category & Rating", {
            'fields': ('category', 'rating')
        }),
        ("Additional info", {
            'fields': ('director_name', 'release_date', 'get_image_html', 'user')
        }),
        ("Creation & modification dates", {
            'fields': ('created_at', 'modified_at'),
            'classes': ('collapse',),
            'description': 'These fields are auto-generated'
        })

    )
