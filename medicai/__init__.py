from flask import Flask
from config.config import ApplicationConfig
from medicai.extensions import db
from medicai.extensions import jwt
from medicai.extensions import migrate
from medicai.extensions import bcrypt
from medicai.extensions import cors
import os


def create_app(config_class=ApplicationConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db, directory='{}/medicai/migrations'.format(os.getcwd()))
    bcrypt.init_app(app)
    cors.init_app(app)

    # Register blueprints here
    from medicai.main import bp as main_bp
    app.register_blueprint(main_bp)

    from medicai.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from medicai.healthRecord import bp as healthRecord_bp
    app.register_blueprint(healthRecord_bp, url_prefix='/healthRecord')


    return app
