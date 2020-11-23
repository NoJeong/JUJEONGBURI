from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.first, name='first'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/review_create/', views.review_create, name='review_create'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
]