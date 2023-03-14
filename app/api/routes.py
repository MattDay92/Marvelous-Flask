from flask import Blueprint, request
from flask_cors import cross_origin
from ..models import User, ReadingList, Favorites, Comments
from werkzeug.security import check_password_hash
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

api = Blueprint('api', __name__)

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@api.route('/api/createuser', methods=["POST"])
def createUser():

    data = request.json
    print(data, 'create user')


    exists = User.query.filter_by(user_id = data['user_id']).first()

    user_id = data['user_id']
    email = data['email']
    name = data['name']
    profile_image = data['profile_image']
    bio = data['bio']
    favorite_char = data['favorite_char']

    user = User(user_id, name, email, profile_image, bio, favorite_char)
    print(user, 'user')

    if exists:
        update = User.query.get(exists.id)
        print(update)
        update.email = email
        update.name = name
        update.profile_image = profile_image
        if bio != 'None':
            update.bio = bio
        if favorite_char != 'None':
            update.favorite_char = favorite_char

        update.updateDB()

    else:
        user.saveToDB()


    return {
        'status': 'ok',
        'message': f"{user.name}'s profile successfully updated!",
        'user': user.to_dict()
    }

@api.route('/api/senduser', methods=["POST"])
def sendProfile():
    
    data = request.json

    user = User.query.filter_by(user_id = data['uid']).first()

    return {
        'status': 'ok',
        'user': user.to_dict()
    }

@api.route('/api/addtoreadinglist', methods=['POST'])
def addToReadingList():
    data = request.json
    print(data)

    user = data['user_id']
    comic = data['comic_id']
    comic_img = data['comic_img']
    comic_title = data['comic_title']

    list = ReadingList(comic, comic_img, comic_title, user)

    list.saveToDB()

    return {
        'status': 'ok',
        'message': f'Successfully added {comic_title} to Reading List'
    }

@api.route('/api/getreadinglist', methods=['POST'])
def getReadingList():
    data = request.json
    print(data)
    user = User.query.filter_by(user_id = data['uid']).first()

    list = [ReadingList.query.get(l.id).to_dict() for l in user.list]

    return {
        'status': 'ok',
        'list': list
    }

@api.route('/api/deletefromreadinglist', methods=['POST'])
def deleteFromReadingList():
    data = request.json
    print(data)
    comic = ReadingList.query.filter_by(user_id = data['uid']).filter_by(comic_id = data['comic_id']).first()

    comic.deleteFromDB()


    user = User.query.filter_by(user_id = data['uid']).first()
    list = [ReadingList.query.get(l.id).to_dict() for l in user.list]

    return {
        'status': 'ok',
        'message': 'Comic successfully removed from Reading List',
        'list': list
    }

@api.route('/api/addtofavorites', methods=['POST'])
def addToFavorites():
    data = request.json
    print(data)

    user = data['user_id']
    comic = data['comic_id']
    comic_img = data['comic_img']
    comic_title = data['comic_title']

    faves = Favorites(comic, comic_img, comic_title, user)

    faves.saveToDB()

    return {
        'status': 'ok',
        'message': f'Successfully added {comic_title} to Favorites'
    }

@api.route('/api/getfavorites', methods=['POST'])
def getFavorites():
    data = request.json
    print(data)
    user = User.query.filter_by(user_id = data['uid']).first()

    faves = [Favorites.query.get(f.id).to_dict() for f in user.favorites]
    print(faves)

    return {
        'status': 'ok',
        'favorites': faves
    }

@api.route('/api/deletefromfavorites', methods=['POST'])
def deleteFromFavorites():
    data = request.json
    print(data)
    comic = Favorites.query.filter_by(user_id = data['uid']).filter_by(comic_id = data['comic_id']).first()

    comic.deleteFromDB()


    user = User.query.filter_by(user_id = data['uid']).first()
    faves = [Favorites.query.get(l.id).to_dict() for l in user.favorites]

    return {
        'status': 'ok',
        'message': 'Comic successfully removed from Favorites',
        'favorites': faves
    }

@api.route('/api/addcomment', methods=['POST'])
def addComment():
    data = request.json
    print(data)

    user = data['user_id']
    comic = data['comic_id']
    comment = data['comment']
    name = data['name']

    comments = Comments(comic, comment, name, user)

    comments.saveToDB()

    return {
        'status': 'ok',
        'message': 'Successfully added Comment'
    }

@api.route('/api/getcomments', methods=['POST'])
def getComments():
    data = request.json
    print(data)
    comic = Comments.query.filter_by(comic_id = data['comic_id']).all()
    print(comic)

    comments = [Comments.query.get(c.id).to_dict() for c in comic]
    print(comments)

    return {
        'status': 'ok',
        'comments': comments
    }

@api.route('/api/deletecomment', methods=['POST'])
def deleteComment():
    data = request.json
    print(data)
    comment = Comments.query.filter_by(id = data['comment_id']).first()

    comment.deleteFromDB()

    comic = Comments.query.filter_by(comic_id = data['comic_id']).all()

    comments = [Comments.query.get(c.id).to_dict() for c in comic]

    return {
        'status': 'ok',
        'message': 'Comic successfully removed from Favorites',
        'comments': comments
    }

