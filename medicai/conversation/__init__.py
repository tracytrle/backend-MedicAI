from flask import Blueprint

bp = Blueprint('conversation', __name__)

from medicai.conversation import routes