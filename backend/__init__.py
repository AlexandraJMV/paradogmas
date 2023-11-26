#https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-song

from flask import Flask
from flask_cors import CORS

"""
Importamos la clase Flask

Usamos el decorador route para decirle a Flask que url activa nuestra función

"""
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

from backend import routes