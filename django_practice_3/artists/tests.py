from django.test import TestCase
from django.core.management import call_command

from artists.orm_exercises import *
from artists.models import Artist, Song


class ORMExerciesTestCase(TestCase):
    def setUp(self):
        call_command('load_initial_data')

    def test_task_1_artist_exists(self):
        """Should return True if there's any artist called Eric Clapton, or False otherwise"""
        artist_exists = task_1_artist_exists()
        assert artist_exists == False

    def test_task_2_first_song_ordered(self):
        """Should return the first Song ordered by title"""
        song = task_2_first_song_ordered()
        assert song.title == 'Castle on the Hill'
        assert song.album_name == 'Divide'
        assert song.artist.artistic_name == 'Ed Sheeran'

    def test_task_3_last_artist_ordered(self):
        """Should return the last Artist ordered by artistic_name"""
        artist = task_3_last_artist_ordered()
        assert artist.artistic_name == 'Stevie Wonders'
        assert artist.first_name == 'Stevland'
        assert artist.last_name == 'Judkins'

    def test_task_4_artist_songs_contains(self):
        """Should return all songs from artist whose artistic names contains the letter X"""
        songs = task_4_artist_songs_contains()
        assert songs.count() == 0  # No songs for artist Jimi Hendrix (only one that has "X" in its name)

    def test_task_5_songs_exclude(self):
        """Should return all songs excluding the ones that contains the word 'Castle' in its title"""
        songs = task_5_songs_exclude()
        assert songs.count() == 2
        assert 'Castle' not in songs[0].title
        assert 'Castle' not in songs[1].title

    def test_task_6_artist_name_starts_with(self):
        """Should return the amount of artists whose artistic name starts with the pattern 'Ji'"""
        assert task_6_artist_name_starts_with() == 1

    def test_task_7_get_or_create_artist(self):
        """
            Should check if Artist 'Eric Clapton' exists in the DB and create it if
            it doesn't. Return True if you had to create, or False otherwise.
        """
        # preconditions
        assert Artist.objects.count() == 3
        assert Artist.objects.filter(artistic_name='Eric Clapton').exists() == False

        response = task_7_get_or_create_artist()

        # postconditions
        assert Artist.objects.count() == 4
        assert Artist.objects.filter(artistic_name='Eric Clapton').exists() == True
        assert response == True  # artist has been created

    def test_task_8_artist_songs_reverse_relationship(self):
        """Should return all songs from artist Stevie Wonders using reverse relationships"""
        songs = task_8_artist_songs_reverse_relationship()
        assert songs.count() == 2
        assert songs[0].artist.artistic_name == 'Stevie Wonders'
        assert songs[1].artist.artistic_name == 'Stevie Wonders'

    def test_task_9_update_song_artist(self):
        """Should create a new Artist and assign it as the owner of the song called Superstition"""
        # preconditions
        song = Song.objects.get(title='Superstition')
        assert song.artist.artistic_name == 'Stevie Wonders'
        assert Artist.objects.count() == 3

        task_9_update_song_artist()

        # postconditions
        song = Song.objects.get(title='Superstition')
        assert song.artist.artistic_name != 'Stevie Wonders'
        assert Artist.objects.count() == 4
