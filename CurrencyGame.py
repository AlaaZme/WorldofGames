import random
from currency_converter import CurrencyConverter
import Score

def play(number,difficulty):

    max_difficulty = 5
    guessed_number = number
    if difficulty > max_difficulty:
        difficulty = max_difficulty
    secret_amount_interval = get_money_interval(difficulty)

    if secret_amount_interval[0] <= guessed_number <= secret_amount_interval[1]:
        Score.add_new_Score(diff, "CurrencyGame")
        return secret_amount_interval[0],"Success"
    else:
        return secret_amount_interval[0],"Fail"


def get_money_interval(difficulty):
    c = CurrencyConverter()
    amount_usd = random.randint(5, 100)
    amount_ils = c.convert(amount_usd, 'USD', 'ILS')
    secret_amount_interval = (amount_ils - (5 - difficulty),
                              amount_ils + (5 - difficulty))
    return secret_amount_interval

