from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin
from medicai.models.user import User
from medicai.extensions import db
from medicai.extensions import bcrypt
from medicai.auth import bp

# @db.route('/user/register', methods=['POST'])
# @cross_origin()
# def user_register():
#   data = request.get_json()
#   user_exists = User.query.filter_by(email=data['email']).first() is not None
#   if user_exists and bcrypt.check_password_hash(user.password, data['password']):
    
