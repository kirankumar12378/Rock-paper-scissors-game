from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

options = ['rock', 'paper', 'scissors']

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.json['choice']
    computer_choice = random.choice(options)
    result = determine_winner(player_choice, computer_choice)
    return jsonify({
        'player': player_choice,
        'computer': computer_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
