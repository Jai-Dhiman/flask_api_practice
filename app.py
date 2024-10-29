from flask import Flask, request
import db

app = Flask(__name__)


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
    name = request.form.get("name")
    width = request.form.get("width")
    height = request.form.get("height")
    return db.photos_create(name, width, height)

@app.route("/photos/<id>.json", methods=["PATCH"])
def update(id):
    name = request.form.get("name")
    width = request.form.get("width")
    height = request.form.get("height")
    return db.photos_update_by_id(id, name, width, height)

@app.route("/photos/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.photos_destroy_by_id(id)