from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre',
                  'release_year', 'watched', 'created_at']
        read_only_fields = ['id', 'created_at', 'owner']
