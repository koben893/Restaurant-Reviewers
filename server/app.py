#!/usr/bin/env python3

# Standard library imports

# Remote library imports

# Local imports
from config import app, db, api
# Add your model imports
from models import Restaurant, User, Review
from flask_restful import Resource
from flask import make_response, jsonify, request
import os

# Views go here!

class Restaurants (Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurants_dict_list = [restaurant.to_dict( rules= ('-reviews',)) for restaurant in restaurants]
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
        users_dict_list = [user._to_dict_(rules = ('reviews',)) for user in users]
        return make_response(users_dict_list)
    
api.add_resource(Users, '/users')

class Reviews (Resource):
    def post (self):
        data = request.get_json()
        try:
            review = Review(
                rating = data['rating'],
                restaurant_id = data ['restaurant_id'],
                user_id = data ['user_id']
            )
        except ValueError as value_error:
            return make_response({"errors": [str(value_error)]}, 422)
        
        db.session.add(review)
        db.session.commit()

        return make_response(review.to_dict(),201)

api.add_resource(Reviews, '/reviews')




@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

