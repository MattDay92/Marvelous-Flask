from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    profile_image = db.Column(db.String)
    bio = db.Column(db.String)
    favorite_char = db.Column(db.String(50))
    list = db.relationship('ReadingList', backref='author', lazy=True)
    favorites = db.relationship('Favorites', backref='author', lazy=True)
    comments = db.relationship('Comments', backref='author', lazy=True)


    def __init__(self, user_id, name, email, profile_image, bio, favorite_char):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.profile_image = profile_image
        self.bio = bio
        self.favorite_char = favorite_char

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def updateDB(self):
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'uid': self.user_id,
            'displayName': self.name,
            'email': self.email,
            'photoURL': self.profile_image,
            'bio': self.bio,
            'favoriteChar': self.favorite_char
        }

class ReadingList(db.Model):
    __tablename__ = 'reading_list'
    id = db.Column(db.Integer, primary_key = True)
    comic_id = db.Column(db.Integer)
    comic_img = db.Column(db.String)
    comic_title = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)

    def __init__(self, comic_id, comic_img, comic_title, user_id):
        self.comic_id = comic_id
        self.comic_img = comic_img
        self.comic_title = comic_title
        self.user_id = user_id

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def updateDB(self):
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'uid': self.user_id,
            'comicId': self.comic_id,
            'image': self.comic_img,
            'title': self.comic_title
        }
    
class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key = True)
    comic_id = db.Column(db.Integer)
    comic_img = db.Column(db.String)
    comic_title = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)

    def __init__(self, comic_id, comic_img, comic_title, user_id):
        self.comic_id = comic_id
        self.comic_img = comic_img
        self.comic_title = comic_title
        self.user_id = user_id

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def updateDB(self):
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'uid': self.user_id,
            'comicId': self.comic_id,
            'image': self.comic_img,
            'title': self.comic_title
        }
    

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comic_id = db.Column(db.Integer)
    comment = db.Column(db.String)
    name = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)

    def __init__(self, comic_id, comment, name, user_id):
        self.comic_id = comic_id
        self.comment = comment
        self.name = name
        self.user_id = user_id

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def updateDB(self):
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'uid': self.user_id,
            'comment': self.comment,
            'name': self.name,
            'comicId': self.comic_id
        }


        
