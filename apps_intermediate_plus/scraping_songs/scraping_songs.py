
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy

from bs4 import BeautifulSoup
import requests

# GET DATE
date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# GET LIST OF TOP SONGS FROM DATE
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}/")
webpage_text = response.text
soup = BeautifulSoup(webpage_text, "html.parser")

result_titles = soup.select("h3.c-title.a-no-trucate")
song_titles = [item.get_text().strip() for item in result_titles]
result_artists = soup.select("span.c-label.a-no-trucate")
song_artists = [item.get_text().strip() for item in result_artists]

# SPOTIFY CREATE PLAYLIST
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.me()['id']
sp.user_playlist_create(user_id, name=date_input, public=True, description="who cares")

# SPOTIFY GET PLAYLIST ID
result = sp.user_playlists(user_id, limit=1, offset=0)
playist_id_ = result["items"][0]["id"]

# SPOTIFY FIND SONG URI
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
song_uri = []
for _ in song_titles:
    number_index = song_titles.index(_)
    title = song_titles[number_index]
    artist = song_artists[number_index]
    search = f"artist: {artist}, track: {title}, "
    result = spotify.search(q=search, limit=1, type='track')
    if result["tracks"]["items"]:
        song_uri.append(result["tracks"]["items"][0]["id"])

# SPOTIFY ADD TRACKS TO PLAYLIST
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
sp.playlist_add_items(playlist_id=playist_id_, items=song_uri)
