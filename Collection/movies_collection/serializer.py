from rest_framework import serializers

from .models import Movie, Director


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = [
            'pk',
            'title',
            'gender',
            'youtube_trailer_url',
            'director',
            'date_added',
            'user',
        ]


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = [
            'director_name'
        ]
