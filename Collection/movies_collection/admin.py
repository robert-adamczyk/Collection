from django.contrib import admin
from django.utils.html import format_html

from  .models import Movie, Director


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title', 'user']
    list_display = ['title', 'gender', 'director', 'user', 'show_youtube_trailer_url', ]
    list_filter = ['title', 'user']

    def show_youtube_trailer_url(self, obj):
        if obj.youtube_trailer_url is not None:
            return format_html(f'<a href="{obj.youtube_trailer_url}" target="_blank">{obj.youtube_trailer_url}</a>')
        else:
            return ''

    show_youtube_trailer_url.short_description = 'Youtube URL'


@admin.register(Director)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['director_name', ]
