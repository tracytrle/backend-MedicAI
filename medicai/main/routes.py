from medicai.main import bp


@bp.route('/medicai')
def index():
    return 'This is The Main Blueprint'
