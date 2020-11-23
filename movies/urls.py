from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.first, name='first'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/movie_search', views.movie_search, name='movie_search'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_pk>/like/', views.like, name='like'),
    path('movies/<int:movie_pk>/review_create/', views.review_create, name='review_create'),
    path('movies/<int:movie_pk>/reviews_delete/<int:review_pk>/', views.reviews_delete, name='reviews_delete'),
]