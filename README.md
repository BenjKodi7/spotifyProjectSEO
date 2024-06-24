# How to Run this Program Properly

#### Set Up:

Installing SQLAlchemy and Pandas Library

 - SQLAlchemy
 https://docs.sqlalchemy.org/en/20/intro.html#installation
 - Pandas
  https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html

 - Spotify API Credentials and Access Token:
https://developer.spotify.com/documentation/web-api/tutorials/getting-started

#### API Security Concerns:

In order to keep your Spotify credentials confidential, 
we need to hide the Client ID and Secret..

Open ".bashrc" so the variables are set every time the terminal re-starts: "sudo nano ~/.bashrc"

Scroll with a scrollwheel or use your arrow keys to get to the bottom of the file and add the variables (Replace variable_value with your information):

export SPOTIFY_CLIENT_ID=[variable_value] \
export SPOTIFY_CLIENT_SECRET=[variable_value]

Press "ctrl" or "command + x" to exit

Run the file so the environments are set for this terminal session: "source ~/.bashrc"

#### Running the File: 
Lastly, run this command "python3 project.py" in the terminal and you should see the API request access code, artist name, and the printed query results

Workflow Badge Status: \
![Status of Styling Workflow](https://github.com/BenjKodi7/spotifyProjectSEO/actions/.github/workflows/main.yaml/badge.svg)
![Status of Testing Workflow](https://github.com/BenjKodi7/spotifyProjectSEO/actions/.github/workflows/test.yaml/badge.svg)

