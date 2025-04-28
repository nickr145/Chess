# Level1Computer.py
import random
from Computer import Computer

class Level1Computer(Computer):
    def make_move(self, board):
        """Level 1 AI: Randomly picks a move."""
        all_moves = []

        for row in board.squares:
            for square in row:
                piece = square.piece
                if piece and piece.color == self.color:
                    valid_moves = piece.get_valid_moves(board)
                    for move in valid_moves:
                        all_moves.append((piece, move))

        if all_moves:
            piece, move = random.choice(all_moves)
            board.move_piece(piece, move[0], move[1])
