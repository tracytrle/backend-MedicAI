from flask import Blueprint

bp = Blueprint('user', __name__)

from medicai.user import routes