# Transformamos los datos a formato json

import os
import json

path_data = "../data/spotify_songs.csv"
archivo = open(path_data, "r", encoding = "utf-8")

data_songs = []

i = 0 
for linea in archivo:
    if i > 0 :
        datos = linea.split(",")
        objeto = {
            "track_name" : datos[1],
            "track_artist" : datos[2],
            "track_popularity" : datos[3],
            "track_album_name" : datos[5],
            "track_album_release_date" : datos[6]
        }
        data_songs.append(objeto)
    i += 1

jsonstring = json.dumps(data_songs)
jsonfile = open("../data/spotify_songs.json", "w")
jsonfile.write(jsonstring)
jsonfile.close()