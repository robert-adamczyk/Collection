from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView, LoginView

from . import views


urlpatterns = [
    path('home/', TemplateView.as_view(template_name='movies_collection/home.html'), name='home-page'),
    # account
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
]
