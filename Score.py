import Utils
import MainScores

'''
def add_Score(diff):
    POINTS_OF_WINNING = (int(diff) * 3) + 5
    print(POINTS_OF_WINNING)
    try:
        with open(Utils.SCORES_FILE_NAME, "a+") as score_file:
            score_file.seek(0)
            score = score_file.read()
            score_file.truncate(0)
            if not score:
                score = 0
            new_score = POINTS_OF_WINNING + int(score)
            score_file.write(str(new_score))
    except Exception as e:
        print("serving score failed New file")
        with open(Utils.SCORES_FILE_NAME, "w") as score_file:
            score_file.write(POINTS_OF_WINNING)
'''

def modify_score(Game_name, newscore):
    score_dict = MainScores.get_scores()
    score_dict[Game_name] = newscore
    return score_dict


def write_dict_to_file(scores_dict):
    total_score = int(scores_dict['total'])
    with open(Utils.NEW_SCORES_FILE_NAME, "w") as file:
        for score in scores_dict:
            file.write(f"{score},{scores_dict[score]}\n")


def add_new_Score(diff, game_name):
    POINTS_OF_WINNING = (int(diff) * 3) + 5
    try:
        new_score = POINTS_OF_WINNING + int(MainScores.get_score_for_game(game_name))
        total_score = int(MainScores.get_score_for_game('total')) + POINTS_OF_WINNING
        score_dict = modify_score(game_name, new_score)
        write_dict_to_file(score_dict)
        total_dict = modify_score("total", total_score)
        write_dict_to_file(total_dict)
    except Exception as e:
        print(e)
        print("serving score failed New file")



