import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt.settings')

import django
django.setup()

import requests

from movies.models import Genre, Movie


apikey = '9518a3d444838dfc19bd751bcc3df303'
lang = 'ko-KR'
page = 1
region = 'KR'

genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={apikey}&language={lang}'
genre_response = requests.get(genre_url).json().get('genres')

# print(genre_response)

for name in genre_response:
    genre = Genre()
    genre.id = name['id']
    genre.name = name['name']
    genre.save()


movie_url = f'https://api.themoviedb.org/3/movie/popular?api_key={apikey}&language=ko&page=2'
movie_response = requests.get(movie_url).json().get('results')

for name in movie_response:
    movie = Movie()
    movie.title = name['title']
    movie.rank = name['vote_average']
    movie.audience = name['popularity']
    movie.poster_url = name['poster_path']
    movie.overview = name['overview']
    movie.original_lang =  name['original_language']
    movie.save()
    for genre in name['genre_ids']:
        movie.genre.add(genre)




