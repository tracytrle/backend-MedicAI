from flask import Blueprint

bp = Blueprint('auth', __name__)

from medicai.auth import routes