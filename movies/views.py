from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse

from .models import Movie
# Create your views here.

def first(request):
    movies = Movie.objects.order_by('pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/first.html', context)


def movie_list (request):
    movies = Movie.objects.order_by('-pk')
    
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)



def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    context= {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
