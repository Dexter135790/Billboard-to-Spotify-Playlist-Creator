import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Webscrapping the top 100 songs according to date
year_input = input("Which year do you want to travel to? Type the date in this format  YYYY-MM-DD: \n")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url = f"https://www.billboard.com/charts/hot-100/{year_input}", headers=header)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")
title_list = soup.select("li ul li h3")
title_list = [title.getText().strip() for title in title_list]

# Gaining access to spotify account

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                                               client_secret=os.getenv("SPOTIFY_SECRET_KEY"),
                                               redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=os.getenv("SPOTIFY_USER_NAME")))

user_id = sp.current_user()["id"]

# Getting song uri's from the title_list

song_uri_list = []

for title in title_list:
    SONG_NAME = title
    SONG_YEAR = year_input.split('-')[0]

    song = sp.search(q=f"track:{SONG_NAME} year:{SONG_YEAR}", type="track")
    try:
        song_uri = song["tracks"]["items"][0]["uri"]
        song_uri_list.append(song_uri)
    except IndexError:
        print(f"{title} doesn't exist on spotify. Skipping it")


# Creating and adding songs to spotify playlist

playlist = sp.user_playlist_create(user=user_id,
                        name=f"{year_input} Billboard 100",
                        public=False,
                        collaborative=False,
                        description="Top 100 songs playlist according to date")

playlist_id = playlist["id"]

add_items = sp.playlist_add_items(playlist_id, items=song_uri_list, position=None)
