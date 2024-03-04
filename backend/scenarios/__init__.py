
from flask import Blueprint

scenarios = Blueprint('scenarios', _name)

@scenarios_bp.route('/scenarios')
def show_library():
    return 'This is the scenarios page.'
