#https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-song
from turtle import title
from flask import Flask, request, jsonify
from waitress import serve
from flask_cors import CORS
import json
from flask import render_template

"""
Importamos la clase Flask

Usamos el decorador route para decirle a Flask que url activa nuestra función

"""
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/',methods=['GET'])
def index():
    jsonFile = open("data/spotify_songs.json", "r")
    datos = (json.load(jsonFile))
    user = {"username" : "Juan José"}

    return render_template("index.html", user = user)
    #return "<h1>heLLOOOOO</h1>"
    #return jsonify(datos)
    # https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

@app.route('/filtro')
def filtro():
    jsonFile = open("data\spotify_songs.json", "r")
    datos = (json.load(jsonFile))
    salida=["aaa"]
    return salida

if __name__ == "__main__":
    app.run(debug=True)
    #serve(app, host="0.0.0.0", port=8080)