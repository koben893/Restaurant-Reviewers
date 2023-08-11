#!/usr/bin/env python3

# Standard library imports

# Remote library imports

# Local imports
from config import app, db, api, bcrypt
# Add your model imports
from models import Restaurant, User, Rating, Review
from flask_restful import Resource
from flask import make_response, jsonify, request, session
import os

# Views go here!

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

class Restaurants (Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurants_dict_list = [restaurant.to_dict( rules= ('-ratings',)) for restaurant in restaurants]
        return make_response (restaurants_dict_list)
    
api.add_resource (Restaurants, '/restaurants')

class RestaurantByID(Resource):
    def get(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if not restaurant:
            return make_response({"error": "Restaurant not found"}, 404)
        return make_response(restaurant.to_dict())
    
    def delete (self, id):
        restaurant = Restaurant.query.filter_by_id(id=id).first()
        if not restaurant:
            return make_response ({"error": "Restaurant not found"},404)
        
        db.session.delete(restaurant)
        db.session.commit()
        return make_response ("", 204)
    
api.add_resource(RestaurantByID, '/restaurants/<int:id>')

class Users (Resource):
    def get (self):
        users = User.query.all()
        users_dict_list = [user._to_dict_(rules = ('ratings',)) for user in users]
        if len(users) == 0:
            return make_response({'error': 'no Users'}, 404)
        return make_response(users_dict_list,200)
    
    def post (self):
        data = request.get_json()
        newUser = User(
            email = data['email'],
            username= data["username"],
            password = data["password"],
            )
        try:
            db.session.add(newUser)
            db.session.commit()
            return make_response (newUser.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
    
api.add_resource(Users, '/users')

class Ratings (Resource):
    def post (self):
        data = request.get_json()
        try:
            rating = Rating(
                rating = data['rating'],
                restaurant_id = data ['restaurant_id'],
                user_id = data ['user_id']
            )
        except ValueError as value_error:
            return make_response({"errors": [str(value_error)]}, 422)
        
        db.session.add(rating)
        db.session.commit()

        return make_response(rating.to_dict(),201)

api.add_resource(Ratings, '/ratings')


class Reviews(Resource):
    def get(self):
        reviews = Review.query.all()
        reviews_dict_list = [review.to_dict() for review in reviews]
        return make_response (reviews_dict_list)
    
api.add_resource (Reviews, '/reviews')



class Login(Resource):
    def post(self):
        request_json = request.get_json()

        username = request_json.get("username")
        password = request_json.get("password")

        user = User.query.filter_by(username = username).first()
        

        if user:
            if user.authenticate(password):
                print(user.id)
                session['user_id'] = user.id
                return user.to_dict(), 200
        else:
            return {'error': 'Invalid Credentials'}, 401
        
api.add_resource(Login, '/login')

class Logout(Resource):
    def delete(self):
        
        if session.get('user_id'):
            
            session['user_id'] = None
            
            return {}, 204
        
        return {'error': '401 Unauthorized'}, 401
    
api.add_resource(Logout, '/logout')








if __name__ == '__main__':
    app.run(port=5557, debug=True)

