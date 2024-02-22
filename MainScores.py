from flask import render_template

import Utils


def score_server():
        with open(Utils.SCORES_FILE_NAME, "r") as show_score:
            return show_score.read()