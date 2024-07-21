from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from medicai.models.user import User
from medicai.extensions import db
from medicai.config.config import ApplicationConfig
from medicai.auth import bp

app = Flask(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@bp.route('/medicai')
def index():
    return jsonify(message="Welcome to MedicAI")

@bp.route('/register', methods=['POST'])
@cross_origin()
def register():
    data = request.get_json()
    user_exists = User.query.filter_by(email=data['email']).first() is not None
    if user_exists:
        return jsonify(message="User already exists"), 409

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        "email": new_user.email,
        "password": data['password']
    })

# Login route
@bp.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'email': user.email})
        return jsonify({
            "id": user.id,
            "email": user.email,
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
