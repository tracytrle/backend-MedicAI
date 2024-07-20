from flask import jsonify

from medicai.auth import bp


@bp.route('/medicai')
def index():
    return jsonify(message="Welcome to MedicAI")
