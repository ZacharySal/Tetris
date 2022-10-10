import copy
import os

import pygame.time

from square import Square
from piece import Piece
from const import *
from config import Config
from sound import Sound


class Board:

    def __init__(self):

        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for row in range(ROWS)]
        self.create_squares()
        self.config = Config()
        self.config.play_music()
        self.pieces = []

        self.game_over = False
        self.level_up = False

        self.completed_rows = 0
        self.score = 0
        self.level = 1

        self.active_piece = None
        self.next_piece = None

    def create_squares(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def update_squares(self):
        for piece in self.pieces:
            for row, col in piece.indices:
                self.squares[row][col].occupied = True

    def clear_squares(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col].occupied = False

    def is_game_over(self):
        for piece in self.pieces:
            if piece != self.active_piece:
                for row, col in piece.indices:
                    if row < 0:
                        self.game_over = True

    def add_piece(self):
        if not self.is_game_over():
            self.config.landed.play()
            if self.next_piece:
                piece = self.next_piece
                self.next_piece = Piece.createRandomPiece()

            else:
                piece = Piece.createRandomPiece()
                self.next_piece = Piece.createRandomPiece()

            self.is_row_complete()
            self.pieces.append(piece)
            self.active_piece = piece
            self.set_piece_outline()
            self.score += (10 * self.level)

    def update_piece(self, direction):
        if self.can_piece_fit(self.active_piece, direction):
            self.active_piece.update_location(direction)
            self.set_piece_outline()

    def fast_drop(self):
        self.active_piece.indices = self.active_piece.trace
        self.add_piece()

    def is_col_empty(self):
        for piece in self.pieces:
            for row, col in piece.indices:
                for test_row, test_col in self.active_piece.indices:
                    if row == test_row + 1 and col == test_col and piece != self.active_piece:
                        return False

        return True

    def shift_pieces_down(self, starting_row):
        new_indices = []

        for piece in self.pieces:
            for row, col in piece.indices:
                if row < starting_row:
                    new_indices.append((row + 1, col))
                elif row > starting_row:
                    new_indices.append((row, col))

            piece.indices = new_indices
            new_indices = []

    def remove_indexes(self, completed_row):
        new_indices = []

        for piece in self.pieces:
            for row, col in piece.indices:
                if not row == completed_row:
                    new_indices.append((row, col))

            piece.indices = new_indices
            new_indices = []

    def is_row_complete(self):
        self.clear_squares()
        self.update_squares()

        for row in range(0, 20, 1):
            row_complete = True
            for col in range(1, 14, 1):
                if self.squares[row][col].occupied is False:
                    row_complete = False

            if row_complete is True:
                self.config.row_complete.play()
                self.remove_indexes(row)
                self.shift_pieces_down(row)
                self.completed_rows += 1
                self.update_squares()
                self.score += (100 * self.level)
                if self.completed_rows % 1 == 0:
                    self.config.level_up.play()
                    self.level += 1
                    if self.level != 11:
                        self.level_up = True

    def create_test_indices(self, curr_piece, direction):

        test_indices = []

        for row, col in curr_piece.indices:
            if direction == ROTATE:
                test_indices = curr_piece.rotate_piece()
                break
            if direction == DOWN:
                test_indices.append((row + 1, col))
            elif direction == LEFT:
                test_indices.append((row, col - 1))
            elif direction == RIGHT:
                test_indices.append((row, col + 1))

        return test_indices

    def can_piece_fit(self, curr_piece, direction, tracing=False):

        test_indices = self.create_test_indices(curr_piece, direction)
        test_pieces = [piece for piece in self.pieces if piece != self.active_piece]

        for test_row, test_col in test_indices:
            if test_col == 0 or test_col == 14:
                return False
            elif test_row > ROWS - 1:
                if not tracing:
                    self.add_piece()
                return False

            for piece in test_pieces:
                for row, col in piece.indices:
                    if row == test_row and col == test_col and not piece.ghost:
                        if not self.is_col_empty() and not tracing:
                            self.add_piece()
                        return False

        return True
    def set_piece_outline(self):

        ghost_piece = copy.deepcopy(self.active_piece)
        self.active_piece.ghost = True

        while self.can_piece_fit(ghost_piece, DOWN, True):
            ghost_piece.update_location(DOWN)

        self.active_piece.trace = ghost_piece.indices
        self.active_piece.ghost = False

        #
        # def ghost_fit(self, curr_piece, direction):
        #
        # test_indices = self.create_test_indices(curr_piece, direction)
        #
        # for test_row, test_col in test_indices:
        #     if test_row > ROWS - 1:
        #         return False
        #     if test_col == 0 or test_col == 14:
        #         return False
        #
        #     for piece in self.pieces:
        #         for row, col in piece.indices:
        #             if row == test_row and col == test_col and not piece.ghost:
        #                 return False
        #
        # return True



