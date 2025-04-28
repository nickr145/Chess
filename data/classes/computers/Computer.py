import random

class Computer:
    def __init__(self, color):
        self.color = color  # 'b' for black, 'w' for white

    def make_move(self, board):
        """ Base computer move logic (to override). """
        raise NotImplementedError("This method should be overridden by subclasses.")
    
