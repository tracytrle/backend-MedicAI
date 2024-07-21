from flask import Flask
from config.config import ApplicationConfig
from medicai.extensions import db
from medicai.extensions import jwt
from medicai.extensions import migrate
import os

def create_app(config_class=ApplicationConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db, directory='{}/medicai/migrations'.format(os.getcwd()))

    # Register blueprints here
    from medicai.main import bp as main_bp
    app.register_blueprint(main_bp)

    from medicai.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
