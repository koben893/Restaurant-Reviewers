from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from flask_restful import Api
from config import db

# Models go here!
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)


class Bar(db.Model, SerializerMixin):
    __tablename__ = 'bar'

    # serialize_rules = ( '-reviews', '-user.reviews', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    

    # Add relationship


    reviews = db.relationship( 'Review', back_populates = 'bar', 
        cascade = 'all, delete-orphan' )

    users = association_proxy( 'reviews', 'user' )

    # Add serialization rules
    
    def __repr__(self):
        return f'<Bar {self.id}: {self.name}>'


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
        if 8 <= new_age <= 18:
            return new_age
        raise ValueError( 'that age got to be between 8 and 18!' )
    
    
    def __repr__(self):
        return f'<user {self.id}: {self.name}>'


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, nullable = False )
    rating = db.Column(db.Integer)

    # Add relationships !!!!!

    user_id = db.Column( db.Integer, db.ForeignKey( 'users.id' ) )
    bar_id = db.Column( db.Integer, db.ForeignKey( 'bars.id' ) )

    user = db.relationship( 'user', back_populates = 'reviews' )
    bar = db.relationship( 'Bar', back_populates = 'reviews' )

    # Add serialization rules
    
    # Add validation
    @validates( 'time' )
    def check_time( self, key, new_time ):
        if 0 <= new_time < 24:
            return new_time
        raise ValueError( 'time must be during an earth day length' )


    def __repr__(self):
        return f'<Review {self.id}>'
