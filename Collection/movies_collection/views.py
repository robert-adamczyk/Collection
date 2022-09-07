#Django
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
#Rest_framework
from rest_framework import viewsets

from .serializer import MovieSerializer, DirectorSerializer
from .forms import RegisterForm
from .models import Director, Movie


def register(request):
    """
        Register new user with automatic login
    """
    if request.method == "GET":
        return render(
            request, 'registration/register.html',
            {'form': RegisterForm}
        )
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home-page')


class MovieListView(ListView):
    model = Movie
    template_name = 'movies_collection/movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies_collection/movie_detail.html'


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movies_collection/form_movie_update.html'
    fields = ['title', 'gender', 'youtube_trailer_url', 'user', 'director']
    success_url = reverse_lazy('movie-list')

    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            form.instance.user = self.request.user
            form.save()
        return redirect('movie-list')


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies_collection/confirm_delete.html'
    success_url = reverse_lazy('movie-list')


@method_decorator(login_required, name='dispatch')
class MovieCreateView(CreateView):
    """
         Add a new movie model to the database
        with auto-adding field of the user
    """
    model = Movie
    template_name = 'movies_collection/movie_form.html'
    fields = ['title', 'gender', 'youtube_trailer_url', 'director']
    success_url = reverse_lazy('movie-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DirectorListView(ListView):
    model = Director
    template_name = 'movies_collection/director_list.html'


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'movies_collection/director_detail.html'


class DirectorUpdateView(UpdateView):
    model = Director
    template_name = 'movies_collection/form.html'
    fields = '__all__'
    success_url = reverse_lazy('director-list')


class DirectorDeleteView(DeleteView):
    model = Director
    template_name = 'movies_collection/confirm_delete.html'
    success_url = reverse_lazy('director-list')


@method_decorator(login_required, name='dispatch')
class DirectorCreateView(CreateView):
    model = Director
    template_name = 'movies_collection/director_form.html'
    fields = '__all__'
    success_url = reverse_lazy('movie-list')


#Rest_api
class MovieApiView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DirectorApiView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = DirectorSerializer





