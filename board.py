import copy
import os

from square import Square
from piece import Piece
from const import *


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for row in range(ROWS)]
        self.create_squares()
        self.pieces = []
        self.game_over = False
        self.active_piece = None

    def create_squares(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def update_squares(self, piece):
        for row, col in piece.indices:
            self.squares[row][col].occupied = True

    def clear_squares(self, piece):
        for row, col in piece.indices:
            self.squares[row][col].occupied = False

    def add_piece(self):
        piece = Piece.createRandomPiece()
        if self.can_piece_fit(piece, 0, spawning=True):
            self.pieces.append(piece)
            self.active_piece = piece
            self.update_squares(piece)
        else:
            self.game_over = True

    def update_piece(self, direction):
        if self.can_piece_fit(self.active_piece, direction):
            self.clear_squares(self.active_piece)
            self.active_piece.update_location(direction)
            self.update_squares(self.active_piece)

    def is_col_empty(self):
        # check if there is piece below col
        for piece in self.pieces:
            for row, col in piece.indices:
                for test_row, test_col in self.active_piece.indices:
                    if row == test_row + 1 and col == test_col and piece != self.active_piece:
                        # print('piece found at', test_row, test_col)
                        return False

        return True

    def is_row_complete(self):
        for row in range(ROWS):
            complete = True
            for col in range(COLS):
                if not self.squares[row][col].occupied:
                    # print(row, col, 'is not occupied')
                    complete = False
                else:
                    # print(row, col, 'is occupied')
                    pass
            if complete:
                print(col, 'is a completed row!')
                for col in range(COLS):
                    self.squares[row][col].occupied = False

    def create_test_indices(self, curr_piece, direction):
        test_indices = []

        for row, col in curr_piece.indices:
            if direction == DOWN:
                test_indices.append((row + 1, col))
            elif direction == LEFT:
                test_indices.append((row, col - 1))
            elif direction == RIGHT:
                test_indices.append((row, col + 1))

        return test_indices

    def can_piece_fit(self, curr_piece, direction, spawning=False):

        if spawning:
            # if piece is spawning test default indices
            test_indices = curr_piece.indices
        elif direction == ROTATE:
            test_indices = curr_piece.rotate_piece()
        else:
            # if not spawning test potential move indices
            test_indices = self.create_test_indices(curr_piece, direction)

        for piece in self.pieces:
            for row, col in piece.indices:
                for test_row, test_col in test_indices:
                    # if piece will collide with another piece that is not itself
                    if row == test_row and col == test_col and piece != self.active_piece:
                        # if column below piece is not empty
                        if self.is_col_empty() is False:
                            if spawning is False:
                                # if piece is not new piece, create new piece
                                self.add_piece()
                            else:
                                # if piece is spawning, and it collides with another piece, game must be over
                                self.game_over = True
                        # piece cannot fit
                        return False
                    # if the test row is greater than the max number of rows
                    elif test_row > ROWS - 1:
                        self.add_piece()
                        return False
                    # if the test col is out of bounds
                    elif test_col == 0 or test_col == 14 or test_row == 0:
                        print(f'{test_col} is 0 or 14')
                        return False
        return True



