import string
import random
import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.length = 9
        self.grid = []
        for x in range(9) :
            self.grid.append(random.choice(string.ascii_uppercase))
        self.high_score = 0



    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if len(word) == 0 :
            return False
        g = self.grid.copy()
        for l in word :
            if l in g :
                g.remove(l)
            else :
                return False
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        j = r.json()
        if j["found"] :
            if len(word) > self.high_score :
                self.high_score = len(word)
            return True
        return False

    def get_high_score(self) -> int :
        return self.high_score


#game = Game()
#print(game.grid) # --> OQUWRBAZE
#my_word = "BAROQUE"
#game.is_valid(my_word) # --> True
