from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .models import Movie, Review
from .forms import ReviewForm
from django.db.models import Q

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


def movie_search(request):
    search_movies=None
    query=None

    if 'q' in request.GET:
        query =request.GET.get('q')
        movies = Movie.objects.all().filter(Q(title__contains=query) | Q(overview__contains=query))
    return render(request, 'movies/index.html', {'query':query, 'movies': movies})




def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    review_form = ReviewForm()
    N=range(5)
    context= {
        'movie': movie,
        'review_form': review_form,
        'reviews' : reviews,
        'video': 'https://www.youtube.com/embed/' + movie.video,
        'N': N,
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



@require_POST
def reviews_delete(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if request.user == review.user:
            review.delete()
    return redirect('movies:movie_detail', movie_pk)



@require_POST
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.like_users.filter(pk=user.pk).exists():
        # if user in article.like_users.all():
            movie.like_users.remove(user)
            liked = False
        else:
            movie.like_users.add(user)
            liked = True

        like_status = {
            'liked': liked,
            'count': movie.like_users.count(),
        }
        return JsonResponse(like_status)
        # return redirect('articles:index')
    return redirect('accounts:login')


