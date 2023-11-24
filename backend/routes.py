from backend import app
from turtle import title
from flask import request, jsonify
from waitress import serve
import json
from flask import render_template, redirect, url_for
import pandas as pd
import numpy as np



#https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-song

@app.route('/qa',methods=['GET', 'POST'])
def aaaa():
    if request.method == 'POST':
        # If the form is submitted via POST
        try:
            # Get the number from the form data
            number = int(request.form['number'])
            data = generate_data(number)
            
        except ValueError:
            return 'Invalid input. Please enter a valid number.'
    return render_template("filtro.html", data = data)



@app.route('/segundoGrafico')
def segundoGrafico():
    return 'Holamundo'

@app.route('/tercerGrafico')
def tercerGrafico():
    return 'Chao mundo'

@app.route('/cuartoGrafico')
def cuartoGrafico():
    return 'Chao mundillo '

@app.route('/filtro')
def filtro():
    dat = request.cookies.get('data')
    print(dat)
    return render_template("filtro.html", data = dat)

@app.route('/', methods =["GET", "POST"])
def getnum():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       numero = request.form.get("numero")
       numero = int(numero)
       data = generate_data(numero)
       redirected = redirect(url_for('.filtro'))
       redirected.set_cookie('data', data)
       
       return redirected
       
    return render_template('index.html')

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
    

