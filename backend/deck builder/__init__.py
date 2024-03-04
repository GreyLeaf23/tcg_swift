from flask import Blueprint

deckbuilderbp = Blueprint('deck_builder', __name)

@deck_builder_bp.route('/deck-builder')
def show_deck_builder():
    return 'This is the deck builder page.'
