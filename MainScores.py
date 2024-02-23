from flask import render_template

import Utils



def score_server():
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as show_score:
            return show_score.read()

    except Exception as e:
        print("error reading scores file")


def get_scores():
    new_scores = {}
    with open(Utils.NEW_SCORES_FILE_NAME, "r") as new_score:
        for score in new_score:
            line = score.split(",")
            name = line[0]
            game_score = line[1]
            new_scores[name] = game_score.strip('\\n\n')
    return new_scores


def get_score_for_game(name):
    score_dict = get_scores()
    return score_dict[name]




'''
@views.route("/Scores")
def Scores():
    try:
        score = MainScores.score_server()
        return render_template('Scores.html', score=score)
    except Exception as e:
        return render_template('ERROR.html')



'''
