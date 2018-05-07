from artists.models import Artist, Song


def artists_filter_by_popularity():
    """Should return all artists that have more than 80 popularity"""
    return Artist.objects.filter(popularity__gt=80)


def artists_get_by_artistic_name():
    """Should return the artist which artistic name is Jimi Hendrix"""
    return Artist.objects.get(artistic_name='Jimi Hendrix')


def songs_delete():
    """Should delete all songs that contain any letter 'a' in its title"""
    Song.objects.filter(title__icontains='a').delete()


def artists_create_song():
    """Should create a new song for Ed Sheeran artist"""
    artist = Artist.objects.get(artistic_name='Ed Sheeran')
    Song.objects.create(
        artist=artist,
        title='Shape of you',
        album_name='Divide'
    )


def artists_order_by_popularity():
    """Should return all artists ordered by popularity"""
    return Artist.objects.all().order_by('popularity')


def song_edit_album():
    """Should take the song with title 'Superstition' and update its album name with any other name"""
    song = Song.objects.get(title='Superstition')
    song.album_name = 'New album'
    song.save()


def song_counter():
    """Should return the amount of songs stored in the database"""
    return Song.objects.count()
