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

    context= {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)



@require_http_methods(['GET', 'POST'])
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review =  form.save(commit=False)
            review.user = request.user
            review.save()
            return  redirect('community:detail', article.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/review_create.html', context)
