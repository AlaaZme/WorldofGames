import random
import Score

def play(number,difficulty):
    print("Game Description:\n"
          "Guess the number between 1 - and Difficulty you entered")
    secret_number = generate_number(difficulty)
    return secret_number,compare_results(number, secret_number,difficulty)

def generate_number(diff):
    return random.randint(1, diff)


def compare_results(secret, user_num, diff):
    if secret == user_num:
        Score.add_new_Score(diff, "GuessGame")
        return "Success"
    else:
        return "Fail"
