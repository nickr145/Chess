import random
from data.classes.computers.Computer import Computer

class Level1Computer(Computer):
    def make_move(self, board):
        all_moves = []

        for square in board.squares:
            piece = square.occupying_piece
            if piece and piece.color == self.color:
                valid_moves = piece.get_valid_moves(board)
                # print(f"{piece.__class__.__name__} at {piece.pos} has {len(valid_moves)} moves.")

                for move in valid_moves:
                    all_moves.append((piece, move))

        # print(f"Computer possible moves: {len(all_moves)}")  # Debugging output

        if all_moves:
            piece, move_square = random.choice(all_moves)
            piece.move(board, move_square, force=True)
        else:
            print("No moves available for computer.")
