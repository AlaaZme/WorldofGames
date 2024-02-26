
import random
import Score

def play(user_list, difficulty, generated_list):
    res = user_list.split(' ')
    return is_list_equal(generated_list, res,difficulty)


def generate_sequence(size):
    secret_list = []
    for _ in range(size):
        secret_list.append(random.randint(1, 101))
    return secret_list


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

