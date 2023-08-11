from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from flask_restful import Api
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt

# Models go here!


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    # serialize_rules = ( '-reviews', '-user.reviews', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    

    # Add relationship


    ratings = db.relationship( 'Rating', back_populates = 'restaurant', cascade = 'all, delete-orphan' )
    users = association_proxy( 'ratings', 'user' )

    # Add serialization rules
    
    def __repr__(self):
        return f'<Restaurant id={self.id} name={self.name}>'


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    # Add serialization rules
    #serialize_rules = ( '-reviews.user', '-reviews.restaurant.reviews' )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String)
    

    # Add relationship
    ratings = db.relationship( 'Rating', back_populates = 'user' )
    restaurants = association_proxy( 'ratings', 'restaurant' )
    
    # Add validation
    @validates( 'name' )
    def validate_name( self, key, new_name ):
        if not new_name:
            raise ValueError('must have a name!')
        return new_name

    @validates( 'age' )
    def validate_age( self, key, new_age ):
        if 21 <= new_age:
            return new_age
        raise ValueError('Must be older than 21')
    
    
    def __repr__(self):
        return f'<user id={self.id} name={self.name}>'
    

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))


class Rating(db.Model, SerializerMixin):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    # date = db.Column(db.String, nullable = False )
    rating = db.Column(db.Integer)

    # Add relationships 

    user_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ) )
    restaurant_id = db.Column( db.Integer, db.ForeignKey( 'restaurants.id' ) )

    restaurant = db.relationship( 'Restaurant', back_populates = 'ratings' )
    user = db.relationship( 'User', back_populates = 'ratings' )

    # Add serialization rules
    serialize_rules =('-user.ratings')
    
    # Add validation
    @validates ('rating')
    def validates_rating(self,key,new_rating):
        if 1 <= new_rating <=5:
            return new_rating
        raise ValueError ('Rating must be between 1 and 5')


    def __repr__(self):
        return f'<Rating {self.id}>'


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    

    # Add relationship


    # Add serialization rules
    
    def __repr__(self):
        return f'<Review id={self.id} name={self.name}>'