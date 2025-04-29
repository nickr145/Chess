import random
from data.classes.computers.Computer import Computer

class Level2Computer(Computer):
    def make_move(self, board):
        """Level 2 AI: Prefer captures if possible."""
        capture_moves = []
        normal_moves = []

        for square in board.squares:
            piece = square.occupying_piece
            if piece and piece.color == self.color:
                valid_moves = piece.get_valid_moves(board)
                for move in valid_moves:
                    if move.occupying_piece and move.occupying_piece.color != self.color:
                        capture_moves.append((piece, move))
                    else:
                        normal_moves.append((piece, move))

        if capture_moves:
            piece, move_square = random.choice(capture_moves)
        elif normal_moves:
            piece, move_square = random.choice(normal_moves)
        else:
            print("No moves available for computer.")
            return

        piece.move(board, move_square, force=True)
