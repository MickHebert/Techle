# simple AI to determine Champ's movements
# I might make all the rooms special classes or functions so that when champ enters the specific sound plays
from random import randint

class AI:
    def __init__(self, level):
        level = self.level

    @property
    def level(self):
        return  self._level

    @level.setter
        def level(self, value):
            self._level = value

    def move(self):
        if self.level < 5:
            move = randint(1, 20)
            if move in range(1, 5):
                Champ.room += 1  # change this, this isnt gonna work


class Champ(AI):
    def __init__(self, level):
        super().__init__(level)

    def room(self):  # maybe have this be inherited from AI, but this wouldnt work, hmm
        rooms = ["outside", "racketball", "bowling", "outside office", "inside office"]

class Tech(AI):
    def __init__(self, level):
        super().__init__(level)


champ = Champ(3)
tech21 = Tech (1)