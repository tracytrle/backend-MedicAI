from flask import jsonify

from medicai.main import bp


@bp.route('/medicai')
def index():
    return jsonify(message="Welcome to MedicAI")
