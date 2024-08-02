import sqlite3
from playsound import playsound


conn = sqlite3.connect('C:\\Users\\Fernando Bernal\\Desktop\\myAppManager\\DB\\artists.db')

cursor = conn.cursor()


def play_song(song_name):
    cursor.execute('''
    SELECT Songs.song_filepath
    FROM Songs
    WHERE Songs.title = ?
    ''', (song_name,))

    song_url = cursor.fetchone()[0]
    playsound(song_url)
    print('playing sound using  playsound')
    print(song_url)


play_song('Hello')
conn.close()


