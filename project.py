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
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
# print(access_token)
headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'

melanin = "6P4kIjBGUzlieJBkUFobTL"
game_changer = "5GxeZ0u1qDX95nZwV055JS"

# # tracks = {"uris": ["spotify:track:" + game_changer, "spotify:track:" + melanin]}
# # playlist_id = "1kT2DU41AV0cK9JQbEm6wS"

getTrack = requests.get(BASE_URL + "tracks/" + melanin, headers=headers)

# # print(addPlaylist.json())

artist_Name = getTrack.json()["album"]["artists"][0]["name"]
print(artist_Name)
# print(getTrack.json())
# print(auth_response_data)