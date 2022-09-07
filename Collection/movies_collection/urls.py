from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView, LoginView

#import django restframework  router
from rest_framework import routers

from . import views

# initializing the router
router = routers.DefaultRouter()

# register each views or route
router.register(r'Directors', views.DirectorApiView, basename='Directors')
router.register(r'Movies', views.MovieApiView, basename='Movies')


urlpatterns = [
    path('home/', TemplateView.as_view(template_name='movies_collection/home.html'), name='home-page'),
    # account
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    # Movie
    path('movie-list', views.MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movie/<int:pk>/edit', views.MovieUpdateView.as_view(), name='movie-edit'),
    path('movie/<int:pk>/delete', views.MovieDeleteView.as_view(), name='movie-delete'),
    path('movie-create/', views.MovieCreateView.as_view(), name='movie-create'),
    # Director
    path('director-list', views.DirectorListView.as_view(), name='director-list'),
    path('director/<int:pk>/', views.DirectorDetailView.as_view(), name='director-detail'),
    path('director/<int:pk>/edit', views.DirectorUpdateView.as_view(), name='director-edit'),
    path('director/<int:pk>/delete', views.DirectorDeleteView.as_view(), name='director-delete'),
    path('director-create/', views.DirectorCreateView.as_view(), name='director-create'),
    # rest_framework
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
