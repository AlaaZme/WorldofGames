NEW_SCORES_FILE_NAME = 'New_score.txt'
BAD_RETURN_CODE = 808

class Game:
    def __init__(self):
        self.Diffuclty = None
        self.secret_list = []

    def set_secret_list(self,secret_list):
        self.secret_list = secret_list

    def get_secret_list(self):
        return self.secret_list

    def set_Diffuclty(self,diff):
        self.Diffuclty = diff

    def get_Diffuclty(self):
        return self.Diffuclty

