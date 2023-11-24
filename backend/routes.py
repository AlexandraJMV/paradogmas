from backend import app
from turtle import title
from flask import request, jsonify
from waitress import serve
import json
from flask import render_template, redirect, url_for

@app.route('/index', methods = ['GET'])
@app.route('/',methods=['GET'])
def index():

    return render_template("index.html")
    #return "<h1>heLLOOOOO</h1>"
    #return jsonify(datos)
    # https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
    #return redirect(url_for('filtro'))
    
@app.route('/filtro')
def filtro():
    jsonFile = open("backend/data/spotify_songs.json", "r", encoding='utf-8')
    datos = (json.load(jsonFile))
    salida=datos
    return salida

@app.route('/segundoGrafico')
def segundoGrafico():
    return 'Holamundo'

@app.route('/tercerGrafico')
def tercerGrafico():
    return 'Holamundo'

@app.route('/cuartoGrafico')
def cuartoGrafico():
    return 'Hola mundo '