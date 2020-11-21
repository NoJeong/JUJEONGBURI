from django.shortcuts import render


from .models import Movie
# Create your views here.

def first(request):
    return render(request, 'movies/first.html')


def movie_list (request):
    movies = Movie.objects.order_by('pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)