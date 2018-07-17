from artists.models import Artist, Song


def task_1_artist_exists():
    """Should return True if there's any artist called Eric Clapton, or False otherwise"""
    # HINT: Use .exists() function
    pass


def task_2_first_song_ordered():
    """Should return the first Song ordered by title"""
    # HINT: Use .first() function
    pass


def task_3_last_artist_ordered():
    """Should return the last Artist ordered by artistic_name"""
    # HINT: Use .last() function
    pass


def task_4_artist_songs_contains():
    """Should return all songs from artist whose artistic names contains the letter X"""
    # HINT: use double underscores "__" to navigate through model's FKs and fields
    pass

def task_5_songs_exclude():
    """Should return all songs excluding the ones that contains the word 'Castle' in its title"""
    # HINT: Use .exclude() function
    pass


def task_6_artist_name_starts_with():
    """Should return the amount of artists whose artistic name starts with the pattern 'Ji'"""
    # HINT: Use __startswith field lookup and .count() function
    pass


def task_7_get_or_create_artist():
    """
        Should check if Artist 'Eric Clapton' exists in the DB and create it if
        it doesn't. Return True if you had to create, or False otherwise.
    """
    # HINT: Use django `get_or_create()` function
    pass


def task_8_artist_songs_reverse_relationship():
    """Should return all songs from artist Stevie Wonders using reverse relationships"""
    # step 1: get Artist "Stevie Wonders"
    artist = '...'

    # step 2: return all songs from that artist using .song_set reverse relationship
    pass


def task_9_update_song_artist():
    """Should create a new Artist and assign it as the owner of the song called Superstition"""
    # step 1: create the artist
    artist = '...'

    # step 2: get the song called 'Superstition'
    song = '...'

    # step 3: assign created artist to the song and save() the song model
    pass
