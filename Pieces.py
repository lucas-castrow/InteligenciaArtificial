class Piece(object):
    def __init__(self, color, pos_x, pos_y):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y

    def possible_movements(self):
        pass
    
class Peao(Piece):
    def __init__(self, color, pos_x, pos_y, first_move = True):
        super().__init__(color, pos_x, pos_y)
        self.first_move = first_move

    def possible_movements(self):
        movements = []
        if self.color == "Black":
            if self.first_move:
                movements.append((self.pos_x+2, self.pos_y))
            movements.append((self.pos_x+1, self.pos_y))
            if self.pos_y + 1 < 8:
                movements.append((self.pos_x+1, self.pos_y+1))
            if self.pos_y - 1 > -1:
                movements.append((self.pos_x+1, self.pos_y-1))
        else:
            if self.first_move:
                movements.append((self.pos_x-2, self.pos_y))
            movements.append((self.pos_x-1, self.pos_y))
            if self.pos_y + 1 < 8:
                movements.append((self.pos_x-1, self.pos_y+1))
            if self.pos_y - 1 > -1:
                movements.append((self.pos_x-1, self.pos_y-1))
        return movements
    def show(self):
        return self.color[0] + "P"

class Torre(Piece):
    def possible_movements(self):
        pass

    def show(self):
        return self.color[0] + "T"

class Cavalo(Piece):
    def possible_movements(self):
        pass

    def show(self):
        return self.color[0] + "C"

class Bispo(Piece):
    def possible_movements(self):
        pass

    def show(self):
        return self.color[0] + "B"

class King(Piece):
    def possible_movements(self):
        pass

    def show(self):
        return self.color[0] + "K"

class Queen(Piece):
    def possible_movements(self):
        pass

    def show(self):
        return self.color[0] + "Q"