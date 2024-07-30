from flask import Blueprint

bp = Blueprint('healthRecord', __name__)

from medicai.healthRecord import routes