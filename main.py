from typing import BinaryIO
import psycopg2
import pandas as pd
import plistlib
import xml.etree.ElementTree as ET
import io
from pathlib import Path
import sqlalchemy
from config import *

def checkKey(dic, key):
    if key in dic.keys():
        return True
    else:
        return False

path = '/Users/paulmalone/Documents/Music Library Project/Library.xml'
file = open(path, "rb")
data = file.read()

lib = plistlib.loads(data)

# for key, value in pl.items():
#     print(key, value)

# print(pl["Playlists"][4]['Name'])

# TRACKS
tracks = []

for item in lib["Tracks"].items():
    tracks.append(item[1])

dft = pd.DataFrame.from_dict(tracks, orient='columns')

# print(dft.columns)

# print(tracks[0][1]["Name"])

# PLAYLISTS
playlists = []
dfp = pd.DataFrame.from_dict(lib["Playlists"])
dfp = dfp.drop('Playlist Items', axis=1)
# print(dfp.columns)
# print(dfp)

# PLAYLIST ITEMS
playlistItems = []
dfPlaylistItems = pd.DataFrame()
# print (pl["Playlists"][8])
# print (pl["Playlists"][8]["Playlist Items"])
# checkKey(pl["Playlists"][8], "Playlist Items")
# print (["Playlist Items"] in pl["Playlists"])
# print (pl["Playlists"][8]["Name"])
for item in lib["Playlists"]:
    if checkKey(item, "Playlist Items"):
        playlistTracks = item["Playlist Items"]
        dfDictionary = pd.DataFrame.from_dict(playlistTracks)
        dfDictionary['Playlist ID'] = item['Playlist ID']
        dfPlaylistItems = pd.concat([dfPlaylistItems, dfDictionary], ignore_index=True)
        # playlistItems.append(dfplaylistTracks)
        # print(playlistTracks)

file.close()

##### Write dataframes to tables in postgres #####

# Create Engine
engine = sqlalchemy.create_engine(f"postgresql://{user}:{password}@{host}:5432/{database}")
# Write Tracks Table
dft.to_sql('tracks', engine, if_exists='replace')

# Write Playlists Table
dfp.to_sql('playlists', engine, if_exists='replace')

# Write Playlist Items Table
dfPlaylistItems.to_sql('playlist_items', engine, if_exists='replace')




# txt = Path(path).read_text()
# # print(txt)
#
# plist = pl.loads(txt)

# plist = b"""<plist version="1.0">
# <dict>
#     <key>foo</key>
#     <string>bar</string>
# </dict>
# </plist>"""
# pl = plistlib.loads(plist)
# print(pl["foo"])