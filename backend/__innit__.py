from flask import Blueprint, rendertemplate

mainbp = Blueprint('main', __name)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/select-game')
def select_game():
    return render_template('select_game.html')
