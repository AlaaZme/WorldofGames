from flask import Blueprint, render_template, request
import Guess_Game
import CurrencyGame
import MainScores
import MemoryGame
from Utils import Game

new_game = Game()
views = Blueprint(__name__, 'views')


@views.route("/")
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return render_template('ERROR.html')

@views.route("/Scores")
def Scores():
    try:
        score_list = MainScores.get_scores()
        return render_template('Scores.html', score=score_list)
    except Exception as e:
        return render_template('ERROR.html')


@views.route("/selectedgame", methods=['POST'])
def selectedgame():
    try:
        new_game.set_name(request.form.to_dict()['name'])
        new_game.set_Diffuclty(request.form.to_dict()['diff'])
        if new_game.get_name() == "MemoryGame":
            new_game.set_secret_list(MemoryGame.generate_sequence(int(new_game.get_Diffuclty())))
        return render_template(f"{new_game.get_name()}.html", game=new_game)
    except Exception as e:
        return render_template('ERROR.html')


@views.route("/result", methods=['POST'])
def result():
    try:
        res = []
        guess = request.form.to_dict()
        if new_game.get_name() == "GuessGame":
            res = Guess_Game.play(int(f"{guess['Guess']}"), int(new_game.get_Diffuclty()))
        elif new_game.get_name() == "CurrencyGame":
            res = CurrencyGame.play(int(f"{guess['Guess']}"), int(new_game.get_Diffuclty()))
        elif new_game.get_name() == "MemoryGame":
            res = MemoryGame.play(guess['Guess'], int(new_game.get_Diffuclty()), new_game.get_secret_list())

        res_dict = {"Guessed": f"{guess['Guess']}", "Secret": res[0], "Result": res[1],
                    "score": MainScores.get_score_for_game(new_game.get_name())}
        return render_template('result.html', res_dict=res_dict)
    except Exception as e:
        return render_template('ERROR.html')
