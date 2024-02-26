import Utils
import MainScores


def modify_score(game_name, newscore):
    score_dict = MainScores.get_scores()
    score_dict[game_name] = newscore
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



