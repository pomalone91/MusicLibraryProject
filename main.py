import pandas as pd
import plistlib
import sqlalchemy
from config import *

# Function to check if a given key exists in a dictionary
def checkKey(dic, key):
    if key in dic.keys():
        return True
    else:
        return False

# Reads the xml file from the given path (path will be unique to your machine. Set it manually yourself. Mine is hiding in a config.py I made with all the db credentials.)
path = xml_path
file = open(path, "rb")
data = file.read()

# Parses the plist file into something we can actually work with (a bunch of lists and dictionaries)
lib = plistlib.loads(data)

# Next three sections are creating the dataframes for tracks, playlists and play list items to map tracks to which playlists they're in

# TRACKS
tracks = []

for item in lib["Tracks"].items():
    tracks.append(item[1])

dft = pd.DataFrame.from_dict(tracks, orient='columns')

# PLAYLISTS
playlists = []
dfp = pd.DataFrame.from_dict(lib["Playlists"])
dfp = dfp.drop('Playlist Items', axis=1)

# PLAYLIST ITEMS
playlistItems = []
dfPlaylistItems = pd.DataFrame()

for item in lib["Playlists"]:
    if checkKey(item, "Playlist Items"):
        playlistTracks = item["Playlist Items"]
        dfDictionary = pd.DataFrame.from_dict(playlistTracks)
        dfDictionary['Playlist ID'] = item['Playlist ID']
        dfPlaylistItems = pd.concat([dfPlaylistItems, dfDictionary], ignore_index=True)

file.close()

# WRITE DATAFRAMES TO TABLES IN POSTGRESQL

# Create Engine
engine = sqlalchemy.create_engine(f"postgresql://{user}:{password}@{host}:5432/{database}")

# Write Tracks Table
dft.to_sql('tracks', engine, if_exists='replace')

# Write Playlists Table
dfp.to_sql('playlists', engine, if_exists='replace')

# Write Playlist Items Table
dfPlaylistItems.to_sql('playlist_items', engine, if_exists='replace')
