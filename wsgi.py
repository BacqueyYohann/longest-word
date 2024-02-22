# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, render_template, request, session
from flask_session import Session
from longest_word.game import Game

app = Flask(__name__)
SESSION_TYPE='filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid)

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    if game.is_valid(word) :
        is_valid = game.is_valid(word)
        set(word)
    #is_valid = game.is_valid(word)
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word, high_score = get())

def set(word):
    session['high_score'] = len(word)
    return

def get():
    if not session.get('high_score') :
        return 0
    return session.get('high_score')
