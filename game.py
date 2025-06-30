
# import player
from player import HumaPlayer,RandomComputerPlayer

class tictaktoe:
    def __init__(self):
        self.board=[" " for _ in range(9)]
        self.current_winner=None

    def print_board(self):

        for i in range(3):
            row = self.board[i*3:(i+1)*3]
            print(" | " + " | ".join(row) + " | ")
        
    
    @staticmethod
    def print_board_nums():
        number_board=[[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        
        for row in number_board:
            print(" | "+" | ".join(row)+" | ")


    def avaliable_move(self):
        return [ i for i,pos in enumerate(self.board) if pos==" "]
    
    def empty_squares(self):
        return " " in self.board
    
    def num_emty_squares(self):
        return self.board.count(" ")
    
    def make_move(self,square,letter):
        if self.board[square] == " ":
            self.board[square]=letter
            if self.winner(square,letter):
                self.current_winner=letter
            return True
        return False
    
    def winner(self,square,letter):
        row_ind=square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([pos==letter for pos in row]):
            return True
        
        col_ind=square%3
        column=[self.board[col_ind+i*3] for i in range(3)]
        if all(pos == letter for pos in column):
            return True
        
        if square%2==0:
            diag1= [self.board[i] for i in [0,4,8]]
            if all(pos == letter for pos in diag1):
                return True

            diag2= [self.board[i] for i in [2,4,6]]
            if all(pos == letter for pos in diag2):
                return True
    
        return False

def play(game,x_player,o_player,print_game):
    if print_game:
        game.print_board_nums()

    letter= "X"#starting letter


    while game.empty_squares:

        if letter=="O":
            square=o_player.get_move(game)
        else:
            square=x_player.get_move(game)


        if game.make_move(square,letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print()

                if game.current_winner:
                    if print_game:
                        print(letter+" wins!!") 
                    return letter ###############
            
            
            if letter=="X":
                letter="O"
            else:
                letter="X"

    if print_game:##########
        print("its a tie")



if __name__=="__main__":
    x_player = HumaPlayer("X")
    o_player = RandomComputerPlayer("O")

    t = tictaktoe()

    play(t,x_player,o_player,True)