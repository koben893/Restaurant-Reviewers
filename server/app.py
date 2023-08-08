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

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

