from django.db import models


GENRE_CHOICES = (
    ("rock", "Rock"),
    ("pop", "Pop"),
)

class Artist(models.Model):
    artistic_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    picture_url = models.URLField(blank=True)
    popularity = models.IntegerField(blank=True)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=255, blank=True)


class Song(models.Model):
    # artist = ...
    title = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255, blank=True)
