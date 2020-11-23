from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .models import Movie, Review
from .forms import ReviewForm
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
    reviews = movie.review_set.all()
    review_form = ReviewForm()
    context= {
        'movie': movie,
        'review_form': review_form,
        'reviews' : reviews,
    }
    return render(request, 'movies/detail.html', context)



@require_POST
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies:movie_detail', movie.pk)
    context = {
        'review_form': review_form,
        'movie': movie,
        'reviews': movie.review_set.all(),
    }
    return render(request, 'movies/detail.html', context)



