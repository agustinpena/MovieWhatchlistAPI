from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.


class MovieListCreateView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    # Set the permission - user must be logged in.
    permission_classes = [permissions.IsAuthenticated]
    queryset = Movie.objects.all()  # Adding this often helps too
    name = 'movie-list'  # This helps the Browsable API identify the view

    # This function ensures we only get the current user's movies
    def get_queryset(self):  # type: ignore
        return Movie.objects.filter(owner=self.request.user)

    # This function automatically sets the owner to the current user when creating a movie
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# This view handles retrieving, updating, and deleting a single movie.
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    # This function ensures users can only access their own movies
    def get_queryset(self):  # type: ignore
        return Movie.objects.filter(owner=self.request.user)
