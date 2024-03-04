from flask import Blueprint

librarybp = Blueprint('library', _name)

@library_bp.route('/library')
def show_library():
    return 'This is the library page.'
