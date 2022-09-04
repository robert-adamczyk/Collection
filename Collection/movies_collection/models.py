from django.db import models
from django.contrib.auth.models import User


GENRES = (
    (1, 'comedy'),
    (2, 'sci-fi'),
    (3, 'romantic'),
    (4, 'horror'),
    (5, 'action'),
)


class Movie(models.Model):
    title = models.CharField(max_length=256)
    gender = models.IntegerField(choices=GENRES, blank=True)
    youtube_trailer_url = models.URLField(null=True, blank=True)
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Director(models.Model):
    director_name = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.director_name

