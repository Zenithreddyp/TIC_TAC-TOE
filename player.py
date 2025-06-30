import random
import math


class Player:
    def __init__(self,letter):
        #letter is X or O
        self.letter=letter

    # we want all players to get there move
    def get_move(self,game):
        pass



class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self,game):
        square=random.choice(game.avaliable_move())
        return square


class HumaPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_spuare=False
        val=None
        while not valid_spuare:
            square= input(self.letter+"'s turmn. Inpt move (0-8): ")
            
            try:
                val=int(square)
                if val not in game.avaliable_move():
                    raise ValueError
                valid_spuare=True
            except ValueError:
                print("please input from avaliable moves")
        
        return val










