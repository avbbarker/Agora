#!/usr/bin/env python3

from models import db, Gallery, Music, UserGallery, UserMusic, User 
from flask_migrate import Migrate
from flask import Flask, request, make_response, jsonify
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Agora</h1>'

#---USER-ROUTES---#################################################################################################################################

@app.get("/users")
def get_users():
    users = User.query.all()
    data = [user.to_dict(rules = ("-user_gallery", "-user_music",)) for user in users]
    return make_response(jsonify(data), 400)

@app.get("/users/<int:id>")
def get_user_by_id(id: int):
    user = User.query.filter(User.id == id).first()
    if not user:
        return make_response(jsonify({"error": "Music not found"}), 404)
    user_dict = user.to_dict(rules = ("-user_gallery", "-user_music",))
    return make_response(jsonify(user_dict),200)

@app.post("/users")
def post_user():
    data = request.get_json()
    try:
        user = User(fname = data["fname"], 
                    lname = data["lname"], 
                    email = data["email"], 
                    dob = data["dob"],
                    username = data["username"],
                    password = data["password"])
        db.session.add(user)
        db.session.commit()
        return make_response(jsonify(user.to_dict(rules = ("-user_gallery", "-user_music",))), 200)
    except:
        return make_response(jsonify({"error": "Validation error"}), 404)

@app.patch("/users/<int:id>")
def patch_users(id: int):
    user = User.query.filter(User.id == id).first()
    if not User:
        return make_response(jsonify({"error": "User not found"}), 404)
    request_data = request.get_json()
    try:
        for key in request_data:
            setattr(user, key, request_data[key])
        db.session.add(user)
        db.session.commit()
        return make_response(jsonify(user.to_dict(rules = ("-user_gallery", "-user_music",))), 202)
    except ValueError:
        return make_response(jsonify({'errors':['validation errors']}), 400)

@app.delete("/user/<int:id>")
def delete_user_by_id(id: int):
    user = User.query.filter(User.id == id).first()
    if not user:
        return make_response(jsonify({"error": "user not found"}), 404)
    db.session.delete(user)
    db.session.commit()
    return make_response(jsonify({}), 200)

#---GALLERY-ROUTES---##############################################################################################################################

@app.get("/galleries")
def get_galleries():
    galleries = Gallery.query.all()
    data = [gallery.to_dict(rules = ("-user_gallery",)) for gallery in galleries]
    return make_response(jsonify(data), 400)

@app.get("/galleries/<int:id>")
def get_gallery_by_id(id: int):
    gallery = Gallery.query.filter(Gallery.id == id).first()
    if not gallery:
        return make_response(jsonify({"error": "Gallery not found"}), 404)
    gallery_dict = gallery.to_dict(rules = ("-user_gallery",))
    return make_response(jsonify(gallery_dict),200)

@app.post("/galleries")
def post_gallery():
    data = request.get_json()
    try:
        gallery = Gallery(title = data["title"], 
                          artist = data["artist"],
                          release_year = data["release_year"],
                          image = data["image"],
                          medium = data["medium"],
                          genre = data["genre"],
                          link = data["link"])
        db.session.add(gallery)
        db.session.commit()
        return make_response(jsonify(gallery.to_dict(rules = ("-user_gallery",))), 200)
    except:
        return make_response(jsonify({"error": "Validation error"}), 404)
    
@app.patch("/galleries/<int:id>")
def patch_gallery(id: int):
    gallery = Gallery.query.filter(Gallery.id == id).first()
    if not gallery:
        return make_response(jsonify({"error": "Gallery not found"}), 404)
    request_data = request.get_json()
    try:
        for key in request_data:
            setattr(gallery, key, request_data[key])
        db.session.add(gallery)
        db.session.commit()
        return make_response(jsonify(gallery.to_dict()), 202)
    except ValueError:
        return make_response(jsonify({'errors':['validation errors']}), 400)

@app.delete("/galleries/<int:id>")
def delete_gallery_by_id(id: int):
    gallery = Gallery.query.filter(Gallery.id == id).first()
    if not gallery:
        return make_response(jsonify({"error": "gallery not found"}), 404)
    db.session.delete(gallery)
    db.session.commit()
    return make_response(jsonify({}), 200)

#---MUSIC-ROUTES---###############################################################################################################################

@app.get("/music")
def get_music():
    music = Music.query.all()
    data = [music.to_dict(rules = ("-user_music",)) for music in music]
    return make_response(jsonify(data), 400)

@app.get("/music/<int:id>")
def get_music_by_id(id: int):
    music = Music.query.filter(Music.id == id).first()
    if not music:
        return make_response(jsonify({"error": "Music not found"}), 404)
    music_dict = music.to_dict(rules = ("-user_music",))
    return make_response(jsonify(music_dict),200)

@app.post("/music")
def post_music():
    data = request.get_json()
    try:
        music = Music(title = data["title"],
                      artist = data["artist"],
                      release_year = data["release_year"],
                      image = data["image"],
                      genre = data["genre"],
                      link = data["link"])
        db.session.add(music)
        db.session.commit()
        return make_response(jsonify(music.to_dict(rules = ("-user_music",))), 200)
    except:
        return make_response(jsonify({"error": "Validation error"}), 404)
    
@app.patch("/music/<int:id>")
def patch_music(id: int):
    music = Music.query.filter(Music.id == id).first()
    if not Music:
        return make_response(jsonify({"error": "Music not found"}), 404)
    request_data = request.get_json()
    try:
        for key in request_data:
            setattr(music, key, request_data[key])
        db.session.add(music)
        db.session.commit()
        return make_response(jsonify(music.to_dict()), 202)
    except ValueError:
        return make_response(jsonify({'errors':['validation errors']}), 400)

@app.delete("/music/<int:id>")
def delete_music_by_id(id: int):
    music= Music.query.filter(Music.id == id).first()
    if not music:
        return make_response(jsonify({"error": "Music not found"}), 404)
    db.session.delete(music)
    db.session.commit()
    return make_response(jsonify({}), 200)

#---ASSOCIATION-ROUTES---#########################################################################################################################

@app.post("/user_gallery")
def post_user_gallery():
    data = request.get_json()
    try:
        user_gallery = UserGallery(price = data["price"], gallery_id = data["gallery_id"], user_id = data["user_id"])
        db.session.add(user_gallery)
        db.session.commit()
        return make_response(jsonify(user_gallery.to_dict(rules = ("-user_gallery",))), 200)
    except:
        return make_response(jsonify({"error": "Validation error"}), 404)
  
@app.post("/user_music")
def post_user_music():
    data = request.get_json()
    try:
        user_music = UserMusic(price = data["price"], music_id = data["music_id"], user_id = data["user_id"])
        db.session.add(user_music)
        db.session.commit()
        return make_response(jsonify(user_music.to_dict(rules = ("-user_music",))), 200)
    except:
        return make_response(jsonify({"error": "Validation error"}), 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)