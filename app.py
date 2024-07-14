# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os
from flask_cors import CORS
from models.user import db, User
from config import ApplicationConfig

app = Flask(__name__)

# Configuration
app.config.from_object(ApplicationConfig)
CORS(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db.init_app(app)


@app.route('/')
def index():
    return "Hello MedicAI"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_exists = User.query.filter_by(email=data['email']).first() is not None
    if user_exists:
        return jsonify(message="User already exists"), 409

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    # return jsonify(message="User created successfully"), 201
    return jsonify({
        "email": new_user.email,
        "password": data['password']
    })

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'email': user.email})
        # return jsonify(access_token=access_token), 200
        return jsonify({
        "id": user.id,
        "email": user.email,
        "access_token": access_token
    }), 200
    else:
        return jsonify(message="Invalid credentials"), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    # print("current user: " + current_user)
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    with app.app_context():
      db.create_all()

    app.run(debug=True)
