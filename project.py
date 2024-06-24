import requests
import json
import os
import sqlalchemy as db
import pandas as pd

AUTH_URL = 'https://accounts.spotify.com/api/token'

# Get client credentials from environment variables
client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

# Check if client credentials are correctly loaded
print(f"Client ID: {client_id}")
print(f"Client Secret: {client_secret}")

# Make a POST request to get the access token
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': {client_id},
    'client_secret': {client_secret},
})

# Print the status code and response
print("Status Code:", auth_response.status_code)
print("Response JSON:", auth_response.json())

# Parse the JSON response
auth_response_data = auth_response.json()

# Check if 'access_token' is in the response
if 'access_token' in auth_response_data:
    access_token = auth_response_data['access_token']
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

    BASE_URL = 'https://api.spotify.com/v1/'

    # Track IDs
    melanin = "6P4kIjBGUzlieJBkUFobTL"
    game_changer = "5GxeZ0u1qDX95nZwV055JS"

    # Get Track (GET)
    response = requests.get(BASE_URL + "tracks/" + melanin, headers=headers)
    artist_Name = response.json()["album"]["artists"][0]["name"]
    print(response.status_code)
    print(artist_Name)

else:
    print("Error: 'access_token' not found in the response.")
    print("Response contains error: " + 
      auth_response_data.get('error', 'No error key'))
)
    print("Error description:", auth_response_data.get('error_description', 'No error description'))


getTrack = pd.DataFrame.from_dict(response.json())

engine = db.create_engine('sqlite:///getTrack.db')

getTrack.to_sql('Track', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM Track;")).fetchall()
    print(pd.DataFrame(query_result))
