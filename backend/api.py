#https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-song
from flask import Flask, request, jsonify
from waitress import serve
from flask_cors import CORS
import json
