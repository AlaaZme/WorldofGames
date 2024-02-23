
import random
import Score

def play(user_list, difficulty, generated_list):
    print(
        "    Game description:\n "
        "The purpose of memory game is to display an amount of random numbers to the users for 0.7\n"
        " seconds and then prompt them from the user for the numbers that he remember. \n"
        "If he was right with all the numbers the user will win otherwise he will lose.\n\n\n")

    res = user_list.split(' ')
    return is_list_equal(generated_list, res,difficulty)


def generate_sequence(size):
    secret_list = []
    for _ in range(size):
        secret_list.append(random.randint(1, 101))
    return secret_list


def parse_list_from_user(user_list):
    while True:

        res = user_list.split(' ')
        num_list = list(filter(None, res))
        try:
            for num in num_list:
                num = int(num)
            return num_list

        except ValueError:
            print("illegal Value re try")


def is_list_equal(secret_list, user_list, diff):
    if len(secret_list) == len(user_list):
        for i in range(len(secret_list)):
            if int(int(user_list[i])) != secret_list[i]:
                return secret_list,"Fail"
        else:
            Score.add_new_Score(diff, "MemoryGame")
            return secret_list,"Success"

    else:
        return secret_list, "Fail"

