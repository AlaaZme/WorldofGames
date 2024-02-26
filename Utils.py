NEW_SCORES_FILE_NAME = 'New_score.txt'
BAD_RETURN_CODE = 808


class Game:
    def __init__(self):
        self.Difficulty = None
        self.secret_list = []
        self.name = ""

    def set_secret_list(self, secret_list):
        self.secret_list = secret_list

    def get_secret_list(self):
        return self.secret_list

    def set_Diffuclty(self, diff):
        self.Difficulty = diff

    def get_Diffuclty(self):
        return self.Difficulty

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name