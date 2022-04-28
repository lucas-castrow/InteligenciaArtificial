#https://readthedocs.org/projects/python-chess/downloads/pdf/stable/
class Game:
    def __init__(self):
        self.start()
    
    def start(self):
        self.current_state = [['.','.','.','.','.','.','.','.'],
                              ['.','.','.','.','.','.','.','.'],
                              ['.','.','.','.','.','.','.','.'],
                              ['.','.','.','.','.','.','.','.'],
                              ['.','.','.','.','.','.','.','.'],
                              ['.','.','.','.','.','.','.','.'],
                              ['.','.','.','.','.','.','.','.'],
                              ['.','.','.','.','.','.','.','.']]