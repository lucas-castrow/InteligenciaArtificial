from Pieces import Peao
from Pieces import Torre
from Pieces import Cavalo
from Pieces import Bispo
from Pieces import Queen
from Pieces import King

class Board:

    def __init__(self):
        self.start()
    
    def start(self):
        self.current_state = [
            [ 0 for i in range(8)] for i in range(8)
        ]
        self.put_peao()
        self.put_torre()
        self.put_cavalo()
        self.put_bispo()
        self.put_king()
        self.put_queen()
    
    def put_peao(self):
        pos_x = 1
        for pos_y in range(8):
            self.current_state[pos_x][pos_y] = Peao('Black', pos_x, pos_y)
        pos_x = 6
        for pos_y in range(8):
            self.current_state[pos_x][pos_y] = Peao('White', pos_x, pos_y)

    def put_torre(self):
        self.current_state[0][0] = Torre('Black', 0, 0)
        self.current_state[0][7] = Torre('Black', 0, 7)
        
        self.current_state[7][0] = Torre('White', 7, 0)
        self.current_state[7][7] = Torre('White', 7, 7)

    def put_cavalo(self):
        self.current_state[0][1] = Cavalo('Black', 0, 1)
        self.current_state[0][6] = Cavalo('Black', 0, 6)
        
        self.current_state[7][1] = Cavalo('White', 7, 1)
        self.current_state[7][6] = Cavalo('White', 7, 6)

    def put_bispo(self):
        self.current_state[0][2] = Bispo('Black', 0, 2)
        self.current_state[0][5] = Bispo('Black', 0, 5)
        
        self.current_state[7][2] = Bispo('White', 7, 2)
        self.current_state[7][5] = Bispo('White', 7, 5)

    def put_king(self):
        self.current_state[0][3] = King('Black', 0, 3)
        
        self.current_state[7][3] = King('White', 7, 3)

    def put_queen(self):
        self.current_state[0][4] = Queen('Black', 0, 4)
        
        self.current_state[7][4] = Queen('White', 7, 4)

    def draw(self):
        for row in self.current_state:
            for column in row:
                if column != 0:
                    print(column.show(), end=' ')
                else:
                    print(column, end='  ')
            print()

board = Board()
board.draw()

print(board.current_state[1][1].possible_movements())