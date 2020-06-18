from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Movie, ExtraInfo
from rest_framework import viewsets
from .serializers import UserSerializer, MovieSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer  


class MovieListView(ListView):
    model = Movie
    template_name = 'movie/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'movies'
    ordering = ['-imdb_rating']
    paginate_by = 5



class MovieDetailView(DetailView):
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'title_eng' ,'content', 'director', 'date_premiere', 'year', 'imdb_rating', 'poster' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = ['title','title_eng' , 'content', 'director', 'date_premiere', 'year', 'imdb_rating', 'poster' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.author:
            return True
        return False


class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    success_url = '/'

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.author:
            return True
        return False

