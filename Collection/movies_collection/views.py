from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.list import ListView

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
