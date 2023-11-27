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

def generate_genre_data(time_intv):
    
    try :
        data_path = "backend/data/spotify_songs.csv"
        data = pd.read_csv(data_path)
        
        colums = ['playlist_subgenre', 'playlist_genre', 'track_album_release_date']
        data = data[colums]
        
        data['date'] = pd.to_datetime(data.track_album_release_date, format='mixed')
        data['year'] = data.date.dt.year
        
        data.loc[ (data.year >= 1957) & (data.year <= 1980), 'time_interv'] = '1957 to 1980'
        data.loc[ (data.year > 1980) & (data.year <= 1990), 'time_interv'] = '1981 to 1990'
        data.loc[ (data.year > 1990) & (data.year <= 2004), 'time_interv'] = '1991 to 2004'
        data.loc[ (data.year > 2004) & (data.year <= 2012), 'time_interv'] = '2005 to 2012'
        data.loc[ (data.year > 2012) & (data.year <= 2016), 'time_interv'] = '2013 to 2016'
        data.loc[ (data.year > 2016) & (data.year <= 2020), 'time_interv'] = '2017 to 2020'

        grouped_data = data.groupby(by=['time_interv', 'playlist_subgenre']).count()
        
        result = grouped_data.loc[time_intv].sort_values(by = 'date', ascending=False)
        return result.date.to_json(orient='split')
    
    except:
        return None
    
def generate_scatter_data(selected_data1, selected_data2):
    data_path = "backend/data/spotify_songs.csv"
    data = pd.read_csv(data_path)
    
    data['label'] = data['track_name']
    
    
    if selected_data1 != selected_data2 :
        new_names = {selected_data1 : 'x', selected_data2 : 'y' }
        
        data =  data[[selected_data1, selected_data2, 'label']]
        data.rename(columns=new_names, inplace=True)
        data = data.sample(1000).to_json(orient='records')
        
        return data
    
    else:
        data['aux'] = data[selected_data1]
        new_names = {selected_data1 : 'x', 'aux' : 'y' }
        
        
        data =  data[[selected_data1, 'aux', 'label']]
        
        data.rename(columns=new_names, inplace=True)
        
        data = data.sample(1000).to_json(orient='records')
        
        return data


# Rutas 

@app.route('/get_data3/<selected_data1>/<selected_data2>')
def get_data3(selected_data1, selected_data2):
    
    if selected_data1 or selected_data2:
        return generate_scatter_data(selected_data1, selected_data2)
    else:
        return jsonify([{'x':1, 'y':2}])


# Recopilamos data para el segundo gráfico
@app.route('/get_data2/<selected_data>')
def get_data2(selected_data):
    if selected_data:
        return generate_genre_data(selected_data)
    else:
        return jsonify([])

# Recopilamos data para el primer gráfico
@app.route('/get_data/<selected_data>')
def get_data(selected_data):
    if selected_data == 'Top Artistas':
        return toptrack_count()
    elif selected_data == 'Últimos Artistas':
        return bottomtrack_count()
    else:
        return jsonify([])

@app.route("/", methods = ["GET", "POST"])
@app.route("/face", methods = ["GET", "POST"])
def face():
    return render_template("face.html")

@app.route('/test')
def test():
    # Dummy data for demonstration
    data = [
        {'x': 1, 'y': 5},
        {'x': 2, 'y': 8},
        {'x': 3, 'y': 12}
        # Add more data as needed
    ]
    
    data = json.dumps(data)
    
    return render_template('scattertest.html', data=data)