import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt.settings')

import django
django.setup()

import requests
import json
from collections import OrderedDict
from movies.models import Genre, Movie


apikey = '9518a3d444838dfc19bd751bcc3df303'
lang = 'ko-KR'
page = 1
region = 'KR'

genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={apikey}&language={lang}'
genre_response = requests.get(genre_url).json().get('genres')


for name in genre_response:
    genre = Genre()
    genre.id = name['id']
    genre.name = name['name']
    genre.save()



movie_list = range(100, 500)
movielist=[]

for n in movie_list:
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=ko-kr".format(n, apikey)
        r = requests.get(url)
        data = json.loads(r.text)
        video_url = "https://api.themoviedb.org/3/movie/{}/videos?api_key={}".format(n, apikey)
        video_r = requests.get(video_url)
        video_data = json.loads(video_r.text)
        print(video_data)
        video_id = video_data["results"][-1]["key"]

        print(n)

        if len(data["overview"]) > 10:
            movie = Movie()
            movie.title = data['title']
            movie.rank = data['vote_average']
            movie.adult = data['adult']
            movie.release_date = data['release_date']
            movie.audience = data['popularity']
            movie.poster_url = data['poster_path']
            movie.overview = data['overview']
            movie.video = video_id
            movie.original_lang =  data['original_language']
            movie.save()
            for genre in data['genres']:
                movie.genre.add(genre['id'])
    except:
        pass

    with open('moviess.json','w',encoding="utf-8") as make_file:
        json.dump(movieData,make_file,ensure_ascii=False,indent="\t")
