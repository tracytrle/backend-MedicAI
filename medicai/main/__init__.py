from flask import Blueprint

bp = Blueprint('main', __name__)

from medicai.main import routes