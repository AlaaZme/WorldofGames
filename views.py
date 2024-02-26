from flask import Blueprint, render_template, url_for, request
import Guess_Game
import CurrencyGame
import MainScores
import MemoryGame
import Utils


new_game = Utils.Game()
views = Blueprint(__name__, 'views')


# GuessGame = Blueprint(__name__,'GuessGame ')
@views.route("/")
def home():
    try:
        #Score.make_scores_file()
        return render_template('index.html')
    except Exception as e:
        return render_template('ERROR.html')


@views.route("/ERROR")
def ERROR():
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
        output = request.form.to_dict()
        new_game.set_Diffuclty(output['diff'])
        diff = new_game.get_Diffuclty()

        if output['name'] == "GuessGame":
            return render_template('GuessGame.html', diff=diff)
        elif output['name'] == "CurrencyGame":
            return render_template('CurrencyGame.html', diff=diff)
        elif output['name'] == "MemoryGame":
            secret_list = MemoryGame.generate_sequence(int(diff))
            new_game.set_secret_list(secret_list)
            return render_template('MemoryGame.html', diff=diff, secret_list=secret_list)
    except Exception as e:
        return render_template('ERROR.html')

@views.route("/result", methods=['POST'])
def result():
    try:
        output = request.form.to_dict()
        diff = new_game.get_Diffuclty()
        res_dict = {}
        if output['name'] == "GuessGame":
            res = Guess_Game.play(int(f"{output['Guess']}"), int(diff))
        if output['name'] == "CurrencyGame":
            res = CurrencyGame.play(int(f"{output['Guess']}"), int(diff))
        if output['name'] == "MemoryGame":
            res = MemoryGame.play(output['Guess'], int(diff),new_game.get_secret_list())

        res_dict = {"Guessed": f"{output['Guess']}", "Secret": res[0], "Result": res[1],
                    "score": MainScores.get_score_for_game(output['name'])}

        return render_template('result.html', res_dict=res_dict)
    except Exception as e:
        print(e)
        return render_template('ERROR.html')
