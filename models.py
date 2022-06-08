import os
from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

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