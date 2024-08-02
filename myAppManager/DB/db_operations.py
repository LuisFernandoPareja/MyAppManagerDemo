import sqlite3

# Connect to a database (or create if not created yet)


# Create a cursor object which will allow me to do operations


# cursor.execute('''
#     SELECT Artists.name
#     FROM Artists
#     JOIN SongArtists ON Artists.artist_id = SongArtists.artist_id
#     WHERE SongArtists.song_id = (
#         SELECT song_id
#         FROM Songs
#         WHERE title = ?
#     )
# ''', ('Song with Multiple Artists',))


def all_songs(artist_name):
    conn = sqlite3.connect('C:\\Users\\Fernando Bernal\\Desktop\\myAppManager\\DB\\artists.db')

    cursor = conn.cursor()
    # Execute the query to retrieve all songs by the artist
    cursor.execute('''
        SELECT Songs.title
        FROM Songs
        JOIN SongArtists ON Songs.song_id = SongArtists.song_id
        JOIN Artists ON SongArtists.artist_id = Artists.artist_id
        WHERE Artists.name = ?
    ''', (artist_name,))

    # Fetch all results
    songs = cursor.fetchall()
    print(songs)
    conn.close()
    return songs


def one_song(song_name):
    conn = sqlite3.connect('C:\\Users\\Fernando Bernal\\Desktop\\myAppManager\\DB\\artists.db')

    cursor = conn.cursor()
    # Execute the query to retrieve all songs by the artist
    cursor.execute('''
            SELECT Songs.title, Songs.song_filepath
            FROM Songs
            JOIN SongArtists ON Songs.song_id = SongArtists.song_id
            JOIN Artists ON SongArtists.artist_id = Artists.artist_id
            WHERE Songs.title = ?
        ''', (song_name,))

    # Fetch all results
    songs = cursor.fetchone()
    print(songs)
    conn.close()
    return songs

one_song('Hello')

# # Define the artist names
# artist_1 = input('Insert name of artist 1: ')
# artist_2 = input('Insert name of artist 2: ')
# artist_names = [artist_1, artist_2]
#
# # Execute the query to retrieve songs by the specified artists
# cursor.execute('''
#     SELECT Songs.title
#     FROM Songs
#     JOIN SongArtists ON Songs.song_id = SongArtists.song_id
#     JOIN Artists ON SongArtists.artist_id = Artists.artist_id
#     WHERE Artists.name IN (?, ?)
#     GROUP BY Songs.title
#     HAVING COUNT(DISTINCT Artists.name) = 2
# ''', artist_names)
#
# # Fetch all results
# songs = cursor.fetchall()
#
# # Print the results
# print(f"Songs by {', '.join(artist_names)}:")
# for song in songs:
#     print(song[0])




