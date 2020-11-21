from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.first, name='first'),
    path('movies/', views.movie_list, name='movie_list'),
]