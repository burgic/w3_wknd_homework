from re import L
from flask import render_template
from app import app
from models.game import *

@app.route('/rock/scissors')
def index():
    return render_template('index.html', title="Play Rock Paper Scissors!")

@app.route('result')
def player_form():
    player1_selection = request.form['player1 - selection']

@app.route('/rock/scissors', methods=['POST'])
def add_option():
    return "Done"