from artists.models import Artist, Song


def task_1_artist_exists():
    """Should return True if there's any artist called Eric Clapton, or False otherwise"""
    if Artist.objects.filter(artistic_name="Eric Clapton").exists():
        return True
    else:
        return False


def task_2_first_song_ordered():
    """Should return the first Song ordered by title"""
    return Song.objects.order_by('title').first()


def task_3_last_artist_ordered():
    """Should return the last Artist ordered by artistic_name"""
    return Artist.objects.order_by('artistic_name').last()


def task_4_artist_songs_contains():
    """Should return all songs from artist whose artistic names contains the letter X"""
    return Song.objects.filter(artist__artistic_name__icontains="x")
    # HINT: use double underscores "__" to navigate through model's FKs and fields
    pass

def task_5_songs_exclude():
    """Should return all songs excluding the ones that contains the word 'Castle' in its title"""
    return Song.objects.all().exclude(title__icontains="castle")


def task_6_artist_name_starts_with():
    """Should return the amount of artists whose artistic name starts with the pattern 'Ji'"""
    return Artist.objects.filter(artistic_name__startswith="Ji").count()


def task_7_get_or_create_artist():
    """
        Should check if Artist 'Eric Clapton' exists in the DB and create it if
        it doesn't. Return True if you had to create, or False otherwise.
    """
    obj, created = Artist.objects.get_or_create(
             artistic_name="Eric Clapton",
            popularity = int(),
            )
    return created


def task_8_artist_songs_reverse_relationship():
    """Should return all songs from artist Stevie Wonders using reverse relationships"""
    artist = Artist.objects.get(artistic_name="Stevie Wonders")
    songs = artist.song_set.all()
    return(songs)


def task_9_update_song_artist():
    """Should create a new Artist and assign it as the owner of the song called Superstition"""
    new_stevie = Artist.objects.create(artistic_name="Stevie Wonder", popularity = 0)
    Song.objects.filter(title='Superstition').update(artist=new_stevie)
