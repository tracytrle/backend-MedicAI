from flask import Flask

from config.config import ApplicationConfig
from medicai.extensions import db


def create_app(config_class=ApplicationConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from medicai.main import bp as main_bp
    app.register_blueprint(main_bp)

    from medicai.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
