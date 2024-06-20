import requests
import json
import re
import os

# CLIENT_ID = "ad6e6b1ab2924df7898e57312ca14813"
# CLIENT_SECRET = "d49229ec920d417a98b068b9cebd0e2b"

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
'grant_type': 'client_credentials',
'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
'client_secret': os.environ.get('SPOTIFY_CLIENT_SECRET'),
"scope": "playlist-modify-public playlist-modify-private"
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headersGet = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'

#Track Ids
melanin = "6P4kIjBGUzlieJBkUFobTL"
game_changer = "5GxeZ0u1qDX95nZwV055JS"

# Get Track (POST)
getTrack = requests.get(BASE_URL + "tracks/" + melanin, headers=headersGet)
artist_Name = getTrack.json()["album"]["artists"][0]["name"]
print(getTrack.status_code)
print(artist_Name)


# # Add Items to a Playlist (POST)
# tracks = {"uris": ["spotify:track:" + game_changer, "spotify:track:" + melanin]}
# playlist_id = "1kT2DU41AV0cK9JQbEm6wS"

# headersPost = {'Authorization': 'Bearer {token}'.format(token=access_token)}
# # print(headersPost)
# addPlaylist = requests.post(BASE_URL + "playlists/" + playlist_id + "/tracks", headers=headersPost)
# print(addPlaylist.json())
