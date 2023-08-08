from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from flask_restful import Api
from config import db

# Models go here!


class Bar(db.Model, SerializerMixin):
    __tablename__ = 'bars'

    # serialize_rules = ( '-reviews', '-user.reviews', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    

    # Add relationship


    reviews = db.relationship( 'Review', back_populates = 'bar', cascade = 'all, delete-orphan' )
    users = association_proxy( 'reviews', 'user' )

    # Add serialization rules
    
    def __repr__(self):
        return f'<Bar id={self.id} name={self.name}>'


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    # Add serialization rules
    #serialize_rules = ( '-reviews.user', '-reviews.bar.reviews' )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column (db.Integer, nullable = False)
    

    # Add relationship
    reviews = db.relationship( 'Review', back_populates = 'user' )
    bars = association_proxy( 'reviews', 'bar' )
    
    # Add validation
    @validates( 'name' )
    def validate_name( self, key, new_name ):
        if not new_name:
            raise ValueError( 'got to have a name!' )
        return new_name

    @validates( 'age' )
    def validate_age( self, key, new_age ):
        if 21 <= new_age:
            return new_age
        raise ValueError( 'Must be older than 21' )
    
    
    def __repr__(self):
        return f'<user id={self.id} name={self.name}>'


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    # date = db.Column(db.String, nullable = False )
    rating = db.Column(db.Integer)

    # Add relationships !!!!!

    user_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ) )
    bar_id = db.Column( db.Integer, db.ForeignKey( 'bars.id' ) )

    bar = db.relationship( 'Bar', back_populates = 'reviews' )
    user = db.relationship( 'User', back_populates = 'reviews' )

    # Add serialization rules
    
    # Add validation
    @validates ('rating')
    def validates_rating(self,key,new_rating):
        if 1 <= new_rating <=5:
            return new_rating
        raise ValueError ('Rating must be between 1 and 5')


    def __repr__(self):
        return f'<Review {self.id}>'
