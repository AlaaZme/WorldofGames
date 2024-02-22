from flask import Blueprint, render_template, url_for, request
import Guess_Game
import  CurrencyGame
views = Blueprint(__name__, 'views')
diff = 0


# GuessGame = Blueprint(__name__,'GuessGame ')
@views.route("/")
def home():
    return render_template('index.html')


@views.route("/selectedgame", methods=['POST'])
def selectedgame():
    output = request.form.to_dict()
    print(output)
    global diff
    diff = output['diff']

    if output['name'] == "GuessGame":
        return render_template('GuessGame.html', diff=diff)

    elif output['name'] == "CurrencyGame":
        return render_template('CurrencyGame.html', diff=diff)


@views.route("/result", methods=['POST'])
def result():

    output = request.form.to_dict()
    print(output)
    user_num = int(f"{output['Guess']}")

    if output['name'] == "GuessGame":
        res = Guess_Game.play(user_num, int(diff))
    elif output['name'] == "CurrencyGame":
        res = CurrencyGame.play(user_num, int(diff))

    res_dict = {"Guessed": f"{output['Guess']}", "Secret": res[0], "Result": res[1]}

    return render_template('result.html', res_dict=res_dict)

