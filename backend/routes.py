from backend import app
from turtle import title
from flask import request, jsonify
from waitress import serve
import json
from flask import render_template, redirect, url_for
import pandas as pd
import numpy as np

# Dataset : https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-song

# Funciones para generación de datos
        # Más adelante : Mover funciones degeneración de datos a un archivo py distinto e importarlos
        
def toptrack_count():
    data_path = "backend/data/spotify_songs.csv"
    cats = ["track_name",
            "track_artist"]

    dataframe = pd.read_csv(data_path, encoding = 'utf-8')[cats]
    tracks_by_artist = dataframe.groupby(by=['track_artist']).count()
    
    # Top 10 artistas según cantidad de canciones
    top10 = tracks_by_artist.sort_values('track_name', ascending = False)['track_name'].head(10)
    top10 = top10.to_json(orient = 'split')
    print(top10)
    return top10

def bottomtrack_count():
    data_path = "backend/data/spotify_songs.csv"
    cats = ["track_name",
            "track_artist"]

    dataframe = pd.read_csv(data_path, encoding = 'utf-8')[cats]
    tracks_by_artist = dataframe.groupby(by=['track_artist']).count()
    
    # Top 10 artistas según cantidad de canciones
    top10 = tracks_by_artist.sort_values('track_name', ascending = True)['track_name'].head(10)
    top10 = top10.to_json(orient = 'split')
    return top10

def generate_data(number):
    data_path = "backend/data/spotify_songs.csv"
    cats = ["track_name",
            "track_artist"]

    dataframe = pd.read_csv(data_path, encoding = 'utf-8')[cats]
    tracks_by_artist = dataframe.groupby(by=['track_artist']).count()
    
    # Top 30 artistas según cantidad de canciones
    top30_tba = tracks_by_artist.sort_values('track_name', ascending = False)['track_name'].head(number)
    top30 = top30_tba.to_json(orient = 'split')
    
    return top30

# Rutas 

@app.route('/getnum', methods =["GET", "POST"])
def getnum():
    if request.method == "POST":
        
        numero = request.form.get("numero")
        if numero.isdigit():
            numero = int(numero)
            data = generate_data(numero)
       
            return render_template('chart.html', data = data)
        else:
            return render_template('error.html', error = 'Ingresó una cadena inválida!!')
       
    return render_template('index.html')

@app.route('/extension', methods = ["POST", "GET"])
def extension():
    if request.method == "POST":                    # Si usamos el método POST vamos a :
        user = request.form["nm"]
        return redirect(url_for("user", usr = user))
    else:                                           # Si usamos el método GET vamos a...
        return render_template('extension.html')

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route('/dinachart')
def dinamic():
    return render_template('dinachart.html')

@app.route('/get_data/<selected_data>')
def get_data(selected_data):s
    if selected_data == 'data1':
        return toptrack_count()
    elif selected_data == 'data2':
        return bottomtrack_count()
    else:
        return jsonify([])
