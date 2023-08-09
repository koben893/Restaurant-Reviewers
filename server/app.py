#!/usr/bin/env python3

# Standard library imports

# Remote library imports

# Local imports
from config import app, db, api
# Add your model imports
from models import Bar, User, Review
from flask_restful import Resource
from flask import make_response, jsonify, request
import os

# Views go here!

class Bars (Resource):
    def get(self):
        bars = Bar.query.all()
        bars_dict_list = [bar.to_dict( rules= ('-reviews',)) for bar in bars]
        return make_response (bars_dict_list)
    
api.add_resource (Bars, '/bars')

class BarByID(Resource):
    def get(self,id):
        bar = Bar.query.filter_by(id=id).first()
        if not bar:
            return make_response({"error": "Bar not found"}, 404)
        return make_response(bar.to_dict())
    
    def delete (self, id):
        bar = Bar.query.filter_by_id(id=id).first()
        if not bar:
            return make_response ({"error": "Bar not found"},404)
        
        db.session.delete(bar)
        db.session.commit()
        return make_response ("", 204)
    
api.add_resource(BarByID, '/bars/<int:id>')

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
                bar_id = data ['bar_id'],
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

