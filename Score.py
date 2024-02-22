
import Utils
import MainScores


def add_Score(diff):
    POINTS_OF_WINNING = (int(diff) * 3) + 5
    print(POINTS_OF_WINNING)
    try:
        with open(Utils.SCORES_FILE_NAME,"a+") as score_file:
            score_file.seek(0)
            score = score_file.read()
            score_file.truncate(0)
            if not score:
                score=0
            new_score = POINTS_OF_WINNING+ int(score)
            score_file.write(str(new_score))
    except FileNotFoundError:
        with open(Utils.SCORES_FILE_NAME,"w") as score_file:
            score_file.write(POINTS_OF_WINNING)


