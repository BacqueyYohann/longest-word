import string
import random


class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.length = 9
        self.grid = []
        for x in range(9) :
            self.grid.append(random.choice(string.ascii_uppercase))



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
        return True


game = Game()
print(game.grid) # --> OQUWRBAZE
#my_word = "BAROQUE"
#game.is_valid(my_word) # --> True
