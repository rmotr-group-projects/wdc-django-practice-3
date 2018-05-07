from django.test import TestCase
from django.core.management import call_command

from artists.orm_exercises import *
from artists.models import Artist, Song


class ORMExerciesTestCase(TestCase):
    def setUp(self):
        call_command('load_initial_data')

    def test_task_1_artists_filter_by_popularity(self):
        """Should return all artists that have more than 80 popularity"""
        # preconditions
        artists = Artist.objects.all()
        artists_popularity = [a.popularity for a in artists]
        assert artists_popularity == [80, 90, 75]

        filtered_artists = task_1_artists_filter_by_popularity()

        # postconditions
        filtered_artists_popularity = [a.popularity for a in filtered_artists]
        assert filtered_artists_popularity == [90]

    def test_task_2_artists_get_by_artistic_name(self):
        """Should return the artist which artistic name is Jimi Hendrix"""
        assert Artist.objects.get(artistic_name='Jimi Hendrix')

        artist = task_2_artists_get_by_artistic_name()
        assert artist.artistic_name == 'Jimi Hendrix'

    def test_task_3_songs_delete(self):
        """Should delete all songs that contain any letter 'a' in its title"""
        # preconditions
        assert Song.objects.count() == 3

        task_3_songs_delete()

        # postconditions
        assert Song.objects.count() == 2
        assert 'a' not in Song.objects.all()[0].title
        assert 'a' not in Song.objects.all()[1].title

    def test_task_4_artists_create_song(self):
        """Should create a new song for Ed Sheeran artist"""
        # preconditions
        assert Song.objects.filter(artist__artistic_name='Ed Sheeran').count() == 1

        task_4_artists_create_song()

        # postconditions
        assert Song.objects.filter(artist__artistic_name='Ed Sheeran').count() == 2

    def test_task_5_artists_order_by_popularity(self):
        """Should return all artists ordered by popularity"""
        artists = task_5_artists_order_by_popularity()
        assert artists[0].popularity == 75
        assert artists[1].popularity == 80
        assert artists[2].popularity == 90

    def test_task_6_song_edit_album(self):
        """Should take the song with title 'Superstition' and update its album name with any other name"""
        # preconditions
        song = Song.objects.get(title='Superstition')
        assert song.album_name == 'Talking book'

        task_6_song_edit_album()

        # postconditions
        song = Song.objects.get(title='Superstition')
        assert song.album_name != 'Talking book'

    def test_task_7_song_counter(self):
        """Should return the amount of songs stored in the database"""
        assert task_7_song_counter() == 3
