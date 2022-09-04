from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import RegisterForm
from .models import Director, Movie


def register(request):
    '''
        Register new user with automatic login
    '''
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
    template_name = 'movies_collection/form.html'
    fields = '__all__'
    success_url = reverse_lazy('movie-list')


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies_collection/confirm_delete.html'
    success_url = reverse_lazy('movie-list')


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movies_collection/movie_form.html'
    fields = '__all__'
    success_url = reverse_lazy('movie-list')


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


class DirectorCreateView(CreateView):
    model = Director
    template_name = 'movies_collection/director_form.html'
    fields = '__all__'
    success_url = reverse_lazy('movie-list')
