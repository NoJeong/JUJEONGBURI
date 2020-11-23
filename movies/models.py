from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    rank = models.IntegerField()
    audience = models.IntegerField()
    adult = models.BooleanField()
    poster_url = models.TextField()
    overview = models.TextField()
    original_lang = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre, symmetrical=False, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)


class Review(models.Model): 
    star = models.IntegerField()
    content = models.TextField()
    star = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)





# class Score(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     content = models.CharField(max_length=140)
#     score = models.IntegerField()
#     movie = models.ForeignKey(Movie, related_name='scores', on_delete=models.CASCADE)