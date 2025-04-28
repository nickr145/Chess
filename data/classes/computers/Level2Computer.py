# Level2Computer.py

import random
from Computer import Computer

class Level2Computer(Computer):
    def make_move(self, board):
        """Level 2 AI: Capture enemy pieces if possible, otherwise random move."""
        capture_moves = []
        regular_moves = []

        for row in board.squares:
            for square in row:
                piece = square.piece
                if piece and piece.color == self.color:
                    valid_moves = piece.get_valid_moves(board)
                    for move in valid_moves:
                        target_row, target_col = move
                        target_square = board.squares[target_row][target_col]
                        if target_square.piece and target_square.piece.color != self.color:
                            # Capture move available
                            capture_moves.append((piece, move))
                        else:
                            regular_moves.append((piece, move))

        if capture_moves:
            # Prioritize capturing
            piece, move = random.choice(capture_moves)
        elif regular_moves:
            # No captures, fallback to random
            piece, move = random.choice(regular_moves)
        else:
            # No possible moves
            return

        board.move_piece(piece, move[0], move[1])
