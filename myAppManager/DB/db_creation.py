import sqlite3

# Connect to a database (or create if not created yet)
conn = sqlite3.connect('artists.db')

# Create a cursor object which will allow me to do operations
cursor = conn.cursor()


# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Artists (
artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NO NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Songs (
song_id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NO NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS SongArtists (
song_id INTEGER ,
artist_id INTEGER,
FOREIGN KEY (song_id) REFERENCES Songs(song_id),
FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
PRIMARY KEY (song_id, artist_id)
)
""")


# Populate tables

cursor.execute('INSERT INTO Artists (name) VALUES (?)', ('The Beatles',))
cursor.execute('INSERT INTO Artists (name) VALUES (?)', ('Adele',))
cursor.execute('INSERT INTO Artists (name) VALUES (?)', ('Beyoncé',))

cursor.execute('INSERT INTO Songs (title) VALUES (?)', ('Hey Jude',))
cursor.execute('INSERT INTO Songs (title) VALUES (?)', ('Hello',))
cursor.execute('INSERT INTO Songs (title) VALUES (?)', ('Song with Multiple Artists',))

cursor.execute('INSERT INTO SongArtists (song_id, artist_id) VALUES (?, ?)', (1, 1))
cursor.execute('INSERT INTO SongArtists (song_id, artist_id) VALUES (?, ?)', (2, 2))
cursor.execute('INSERT INTO SongArtists (song_id, artist_id) VALUES (?, ?)', (3, 1))
cursor.execute('INSERT INTO SongArtists (song_id, artist_id) VALUES (?, ?)', (3, 3))

# Commit the changes
conn.commit()

# Retrieve data
cursor.execute('''
    SELECT Artists.name
    FROM Artists
    JOIN SongArtists ON Artists.artist_id = SongArtists.artist_id
    WHERE SongArtists.song_id = (
        SELECT song_id
        FROM Songs
        WHERE title = ?
    )
''', ('Song with Multiple Artists',))

artists = cursor.fetchall()
print(artists)

# Close the connection
conn.close()

