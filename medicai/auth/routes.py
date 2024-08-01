from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin
from medicai.models.user import User
from medicai.extensions import db
from medicai.extensions import bcrypt
from medicai.auth import bp


@bp.route('/medicai')
def index():
    return jsonify(message="Welcome to MedicAI")


@bp.route('/register', methods=['POST'])
@cross_origin()
def register():
    data = request.get_json()
    if 'phone' not in data:
        return jsonify(message="Phone number is required"), 400
    if 'email' not in data:
        return jsonify(message="Email is required"), 400
    if 'password' not in data:
        return jsonify(message="Password is required"), 400
    
    existing_user_by_phone = User.query.filter_by(phone=data['phone']).first() is not None
  
    if existing_user_by_phone:
        return jsonify(message="User with this phone number already exists"), 409
    
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
        email=data['email'], 
        password=hashed_password, 
        phone=data['phone'],
        firstName=data.get('firstName', ''), 
        middleName=data.get('middleName', ''), 
        lastName=data.get('lastName', ''), 
        gender=data.get('gender', ''), 
        dateOfBirth=data.get('dateOfBirth', ''), 
        city=data.get('city', ''), 
        country=data.get('country', '')
    )
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        "email": new_user.email,
        "phone": new_user.phone,
        "password": data['password']
    })

# Login route
@bp.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    if 'phone' not in data:
        return jsonify(message="Phone number is required"), 400
    if 'email' not in data:
        return jsonify(message="Email is required"), 400
    if 'password' not in data:
        return jsonify(message="Password is required"), 400

    user = User.query.filter_by(phone=data['phone']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'phone': user.phone})
        return jsonify({
            "id": user.id,
            "email": user.email,
            "phone": user.phone,
            "access_token": access_token
        }), 200
    else:
        return jsonify(message="Invalid credentials"), 401


@bp.route('/protected', methods=['GET'])
@cross_origin()
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
