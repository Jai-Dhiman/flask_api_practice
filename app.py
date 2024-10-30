from flask import Flask, request
from flask_cors import CORS
import db


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/photos.json")
def index():
    return db.photos_all()

@app.route("/photos/<id>.json")
def show(id):
    return db.photos_find_by_id(id)

@app.route("/photos.json", methods=["POST"])
def create():
    data = request.get_json()
    name = data.get("name")
    width = data.get("width")
    height = data.get("height")
    url = data.get("url")
    return db.photos_create(name, width, height, url)

@app.route("/photos/<id>.json", methods=["PATCH"])
def update(id):
    data = request.get_json() 
    name = data.get("name")
    width = data.get("width")
    height = data.get("height")
    url = data.get("url") 
    return db.photos_update_by_id(id, name, width, height, url) 

@app.route("/photos/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.photos_destroy_by_id(id)