from flask import Flask
from main import main_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
@app.route('/')
def index(): 
    return 'Hello, World! This is your Flask app'

@app.route('/pokemon')
def pokemon():
    return 'This is the Pokemon page.'

@app.route('/deck-builder')
def deck_builder():
    return 'This is the deck builder page.'

if __name__ == '__main__':
    app.run(debug=True)
    
    
