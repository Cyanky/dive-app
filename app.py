import sys
import json
import os
from unittest import result
from urllib import response
from flask_cors import CORS
# from models import setup_db

import urllib.request
from werkzeug.utils import secure_filename
from asyncio.format_helpers import _get_function_source
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, ForeignKey
import logging
from logging import Formatter, FileHandler



from form import MusicianForm
from flask_wtf import FlaskForm
from form import *
from sqlalchemy import func


import datetime
import random

from werkzeug.utils import secure_filename
import time
import base64

from auth import AuthError, requires_auth, get_token_auth_header

# from flask_migrate import Migrate
# migrate = Migrate()
# migrate.init_app(application, db)


# https://dev-dc7i9qu0.us.auth0.com/authorize?audience=divemusic&response_type=token&client_id=6Tspmj0FPydwzQoAnI66ZdioqSgOoJcF&redirect_uri=https://127.0.0.1:5000/musicians/create



# UPLOAD_FOLDER = 'static/uploads'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# def allowed_file(filename):
# 	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# class Pic_str:
#     def create_uuid(self): #生成唯一的图片的名称字符串，防止图片显示时的重名问题
#         nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S");  # 生成当前时间
#         randomNum = random.randint(0, 100);  # 生成的随机整数n，其中0<=n<=100
#         if randomNum <= 10:
#             randomNum = str(0) + str(randomNum)
#         uniqueNum = str(nowTime) + str(randomNum)
#         return uniqueNum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sawzrcjjllmcwb:3275998379c87b87f6d3899cbac4b767f229a56a233624fef970bc8f532ff732@ec2-52-72-99-110.compute-1.amazonaws.com:5432/db2gbfccp2e5u0'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:abc@localhost:5432/diveapp'
app.config.from_object('config')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# def create_app(test_config=None):

#     app = Flask(__name__)
#     setup_db(app)
#     CORS(app)

# ------------------------------------------------------------------------------#
# Data Model
# ------------------------------------------------------------------------------#




class Musician(db.Model):
    __tablename__ = 'musician'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    e_mail = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(500))
    introduction = db.Column(db.String(120))
    avatar_link = db.Column(db.String())
    genres = db.Column(db.String(120))
    songs = db.relationship('Song', backref='musicians', lazy=True, cascade="save-update, merge, delete")
    

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.update(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<Musician {self.name}>"

# class Genre(db.Model):
#     __tablename__ = 'genre'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False)
#     songs = db.relationship('Song', backref='genres', lazy=True, cascade="save-update, merge, delete")

#     def add(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.update(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

#     def __repr__(self):
#         return f"<Genre {self.name}>"


class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    introduction = db.Column(db.String(120))
    cover_link = db.Column(db.String())
    song_link = db.Column(db.String(500))
    genre = db.Column(db.String(120))
    musician_id = db.Column(db.Integer, db.ForeignKey('musician.id'))


    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.update(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<Song {self.name}>"

# db.create_all()

# ------------------------------------------------------------------------------#
# Controllers
# ------------------------------------------------------------------------------#

@app.route('/')
def index():
    return render_template('pages/home.html')

#  Musicians
# ------------------------------------------------------------

@app.route('/musicians')
def musicians():
    data = Musician.query.with_entities(Musician.id, Musician.name, Musician.avatar_link).all()
    return render_template('pages/musician.html', musicians=data)

@app.route("/musicians/<int:musician_id>")
# @requires_auth('get:musician-detail')
def show_musician(musician_id):
    musician = Musician.query.get(musician_id)

    if not musician:
        
        return render_template("errors/404.html")
    
    songs = []
    # genres = []
    

    # for song in (
    #     db.session.query(Song)
    #     .join(Genre)
    #     .filter(Song.musician_id == musician_id)
    #     .all()
    # ):
    #     genres.append(
    #         {
    #             "genre_id": song.genre_id,
    #             "genre_name": song.genres.name,

    #         }
    #     )

    for song in (
        db.session.query(Song)
        .join(Musician)
        .filter(Song.musician_id == musician_id)
        .all()
    ):
        songs.append(
            {
                "song_id": song.id,
                "song_name": song.name,
                "song_cover": song.cover_link,
                "song_introduction": song.introduction,
                "song_genre": (song.genre).split(","),
                "song_link": song.song_link,
            }
        )



    data = {
        "id": musician.id,
        "name": musician.name,
        "e_mail": musician.e_mail,
        "phone": musician.phone,
        "website": musician.website,
        "introduction": musician.introduction,
        "avatar": musician.avatar_link,
        "genres": (musician.genres).split(","),
        "songs": songs,
    }

    return render_template("pages/show_musician.html", musician=data)



# Create Musicians
# ------------------------------------------------------------

@app.route('/musicians/create', methods=['GET'])
@requires_auth('get:musician-create-page')
def create_musician_form():
    form = MusicianForm()
    return render_template("forms/new_musician.html", form=form)

@app.route("/musicians/create", methods=['POST'])
@requires_auth('post:musician')
def create_musician_submission():
    genresList = request.form.getlist("genres")
    musicianData = MusicianForm(request.form)
    
    try:
        newMusician = Musician()
        newMusician.name=musicianData.name.data,
        newMusician.e_mail=musicianData.e_mail.data,
        newMusician.phone=musicianData.phone.data,
        newMusician.website=musicianData.website.data,
        newMusician.introduction=musicianData.introduction.data,
        newMusician.avatar_link=musicianData.avatar_link.data,
        newMusician.genres=",".join(genresList)

        newMusician.add()
        flash("Musician: " + newMusician.name + " has been successfully listed!")
    except:
        db.session.rollback()
        print(sys.exc_info)
        flash("An error occurred. Musician " + newMusician.name + " could not be listed.")
    finally:
        db.session.close()
    return render_template("forms/new_musician.html")




# Upload files
# ------------------------------------------------------------

# @app.route('/musicians/avatar')
# def upload_form():
#     return render_template('forms/upload_avatar.html')

# @app.route('/musicians/avatar', methods=['POST'])
# def upload_image():
    

# 	if 'file' not in request.files:
# 		flash('No file part')
# 		return redirect(request.url)
# 	file = request.files['file']
    
# 	if file.filename == '':
# 		flash('No image selected for uploading')
# 		return redirect(request.url)
# 	if file and allowed_file(file.filename):
# 		filename = Pic_str.create_uuid(secure_filename(file.filename))   
# 		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# 		flash('Image successfully uploaded')
# 		return render_template('forms/upload_avatar.html', filename=filename)
# 	else:
# 		flash('Allowed image types are -> png, jpg, jpeg, gif')
# 		return redirect(request.url)

# @app.route('/up_photo', methods=['POST'], strict_slashes=False)
# def api_upload():
#     file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
#     if not os.path.exists(file_dir):
#         os.makedirs(file_dir)
#     f = request.files['photo']
#     if f and allowed_file(f.filename):
#         fname = secure_filename(f.filename)
#         print fname
#         ext = fname.rsplit('.', 1)[1]
#         new_filename = Pic_str().create_uuid() + '.' + ext
#         f.save(os.path.join(file_dir, new_filename))

#         return jsonify({"success": 0, "msg": "上传成功"})
#     else:
#         return jsonify({"error": 1001, "msg": "上

# @app.route('/display/<filename>')
# def display_image(filename):
# 	#print('display_image filename: ' + filename)
# 	return redirect(url_for('static', filename='uploads/' + filename), code=301)

# Songs 
# ------------------------------------------------------------
@app.route('/songs')
def songs():
    data = []
    for song in db.session.query(Song).join(Musician).all():
        data.append(
            {
                "id": song.id,
                "name": song.name,
                "cover_link": song.cover_link,
                "song_link": song.song_link,
                "genre": song.genre,
                "musician": song.musicians.name,
                "musician_id": song.musicians.id,
            }
        )
    return render_template('pages/song.html', songs=data)

# Create songs 
# ------------------------------------------------------------

@app.route('/songs/create', methods=['GET'])
# @requires_auth('get:song-create-page')
def create_song_form():
    form = SongForm()
    return render_template("forms/new_song.html", form=form)

@app.route("/songs/create", methods=['POST'])
# @requires_auth('post:song')
def create_song_submission():
    genresList = request.form.getlist("genres")
    songData = SongForm(request.form)
    
    try:
        newSong = Song()
        newSong.name=songData.name.data,
        newSong.cover_link=songData.cover_link.data,
        newSong.song_link=songData.song_link.data,
        newSong.introduction=songData.introduction.data,
        newSong.musician_id=songData.musician_id.data,
        
        newSong.genre=",".join(genresList)

        newSong.add()
        flash("Song: " + newSong.name + " has been successfully listed!")
    except:
        db.session.rollback()
        print(sys.exc_info)
        flash("An error occurred. Song " + newSong.name + " could not be listed.")
    finally:
        db.session.close()
    return render_template("forms/new_song.html")








# Search 
# ------------------------------------------------------------
@app.route('/search')
def search():
    return render_template('pages/search.html')


@app.route('/search/song')
def search_song():
    return render_template('pages/search_song.html')

@app.route('/search/musician')
def search_musician():
    return render_template('pages/search_musician.html')

@app.route('/search/song', methods=["POST"])
def search_song_results():
    search_term = request.form.get("search_term", "")
    results = Song.query.filter(Song.name.ilike(f"%{search_term}%")).all()
    if not results:
        
        return render_template("errors/404.html")
    
    data = []
    for result in results:
        data.append(
            {
                "id": result.id,
                "name": result.name,
                "cover_link": result.cover_link,
                "song_link": result.song_link,
                "musician": result.musicians.name,
                "musician_id": result.musicians.id,

            }
        )
    
    return render_template(
        "pages/search_song_results.html",
        results=data,
        search_term=request.form.get("search_term", "")
    )

@app.route('/search/musician', methods=["POST"])
def search_musician_results():
    search_term = request.form.get("search_term", "")
    results = Musician.query.filter(Musician.name.ilike(f"%{search_term}%")).all()
    if not results:
        
        return render_template("errors/404.html")
    
    data = []
    for result in results:
        data.append(
            {
                "id": result.id,
                "name": result.name,
                "avatar_link": result.avatar_link,

            }
        )
    
    return render_template(
        "pages/search_musician_results.html",
        results=data,
        search_term=request.form.get("search_term", "")
    )

#  Update
#  ----------------------------------------------------------------
@app.route("/musicians/<int:musician_id>/edit", methods=["GET"])
def edit_musician(musician_id):
    form = MusicianForm()
    musician = Musician.query.get(musician_id)

    if not musician:
        flash("This musician does not exist.")
        return render_template("errors/404.html")

    form.name.data = musician.name
    form.phone.data = musician.phone
    form.e_mail.data = musician.e_mail
    form.website.data = musician.website
    form.avatar_link.data = musician.avatar_link
    form.genres.data = musician.genres
    form.introduction.data = musician.introduction
    # Done: populate form with fields from artist with ID <artist_id>
    return render_template("forms/edit_musician.html", form=form, musician=musician)


@app.route("/musicians/<int:musician_id>/edit", methods=["POST"])
# @requires_auth('post:edit-musician')
def edit_musician_submission(musician_id):
    # Done: take values from the form submitted, and update existing
    # artist record with ID <artist_id> using the new attributes
    musician = Musician.query.get(musician_id)
    musicianData = MusicianForm(request.form)
    genresList = request.form.getlist("genres")
    try:
        musician.name = musicianData.name.data
        musician.avatar_link = musicianData.avatar_link.data
        musician.phone = musicianData.phone.data
        musician.genres = ",".join(genresList)
        musician.website = musicianData.website.data
        musician.e_mail = musicianData.e_mail.data
        musician.introduction = musicianData.introduction.data

        db.session.commit()
        # on successful db update, flash success
        flash("Artist: " + musicianData.name.data + " has been successfully updated!")
    except:
        db.session.rollback()
        print(sys.exc_info())
        # Done: on unsuccessful db update, flash an error instead.
        flash(
            "An error occurred. Artist "
            + musicianData.name.data
            + " could not be updated."
        )
    finally:
        db.session.close()
    return redirect(url_for("show_musician", musician_id=musician_id))

@app.route("/songs/<int:song_id>/edit", methods=["GET"])
def edit_song(song_id):
    form = SongForm()
    song = Song.query.get(song_id)

    if not song:
        flash("This song does not exist.")
        return render_template("errors/404.html")

    form.name.data = song.name
    form.song_link.data = song.song_link
    form.cover_link.data = song.cover_link
    form.genres.data = song.genre
    form.introduction.data = song.introduction
    form.musician_id.data = song.musician_id
    # Done: populate form with fields from artist with ID <artist_id>
    return render_template("forms/edit_song.html", form=form, song=song)


@app.route("/songs/<int:song_id>/edit", methods=["POST"])
# @requires_auth('post:edit-song')
def edit_song_submission(song_id):
    # Done: take values from the form submitted, and update existing
    # artist record with ID <artist_id> using the new attributes
    song = Song.query.get(song_id)
    songData = SongForm(request.form)
    try:
        song.name = songData.name.data
        song.song_link = songData.song_link.data
        song.cover_link = songData.cover_link.data
        song.genre = songData.genres.data 
        song.musician_id = songData.musician_id.data
        song.introduction = songData.introduction.data

        db.session.commit()
        # on successful db update, flash success
        flash("Song: " + songData.name.data + " has been successfully updated!")
    except:
        db.session.rollback()
        print(sys.exc_info())
        # Done: on unsuccessful db update, flash an error instead.
        flash(
            "An error occurred. Song "
            + songData.name.data
            + " could not be updated."
        )
    finally:
        db.session.close()
    return render_template("pages/song.html")

# Delete 
# ------------------------------------------------------------

# @app.route("/musicians/<musician_id>/delete")
# def delete_musician(musician_id):
#     musician = Musician.query.get(musician_id)

#     data = {
#             "id": musician.id,
#             "name":musician.name,
#     }
        
#     return render_template("forms/delete_musician.html", musician=data)

# @app.route("/musicians/<musician_id>/delete", methods=["DELETE"])
# def delete_musician_confirm(musician_id):
#     error = False
#     try:
#         musician = Musician.query.get(musician_id)
#         musicianName = musician.name
#         db.session.delete(musician_id)
#         db.session.commit()
#     except:
#         error = True
#         db.session.rollback()
#         print(sys.exc_info())
#     finally:
#         db.session.close()

#     if error:
#         flash(f"{musicianName} could not be deleted.")
#     else:
#         flash(f"{musicianName} has been successfully deleted.")
#     return render_template("pages/musician.html")

# @app.route("/songs/<song_id>/delete")
# def delete_song(song_id):
#     song = Song.query.get(song_id)

#     data = {
#             "id": song.id,
#             "name":song.name,
#     }
        
#     return render_template("forms/delete_song.html", song=data)

# @app.route("/songs/<song_id>/delete", methods=["DELETE"])
# def delete_song_confirm(song_id):
#     error = False
#     try:
#         song = Song.query.get(song_id)
#         songName = song.name
#         db.session.delete(song_id)
#         db.session.commit()
#     except:
#         error = True
#         db.session.rollback()
#         print(sys.exc_info())
#     finally:
#         db.session.close()

#     if error:
#         flash(f"{songName} could not be deleted.")
#     else:
#         flash(f"{songName} has been successfully deleted.")
#     return render_template("pages/song.html")



# @app.route("/songs/<ing:song_id>/delete", methods=["DELETE"])
# def delete_song(song_id):
#     error = False
#     try:
#         song = Song.query.get(song_id)
#         songName = song.name
#         song.delete()
#     except:
#         error = True
#         db.session.rollback()
#         print(sys.exc_info())
#     finally:
#         db.session.close()

#     if error:
#         flash(f"{songName} could not be deleted.")
#     else:
#         flash(f"{songName} has been successfully deleted.")
#     return render_template("layouts/main.html")

# if not app.debug:
#     file_handler = FileHandler("error.log")
#     file_handler.setFormatter(
#         Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]")
#     )
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info("errors")


# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#
# return app

# app = create_app()
# Default port:
if __name__ == "__main__":
    app.run()

# Or specify port manually:
"""
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
"""