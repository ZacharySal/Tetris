import math
import random
import os
from const import *


class Piece:

    def __init__(self, indices, anchor, img_path):
        self.indices = indices
        # self.color = random.choice(COLORS)
        self.img_path = img_path
        self.anchor = anchor
        self.origin = (0, 0)
        self.row_offset = 0
        self.col_offset = 0
        self.trace = []
        self.ghost = False
        self.rotations = []
        self.rotation_index = 0


    def update_possible_rotations(self):
        if self.rotation_index == 0:
            self.rotations.append((-1, 0))
            self.rotations.append((-1, 1))
            self.rotations.append((0, 2))
            self.rotations.append((-1, 2))

    def update_origin(self):
        row = self.anchor[0] + self.row_offset
        col = self.anchor[1] + self.col_offset
        self.origin = (row, col)

    def update_offset(self, direction):
        if direction == DOWN:
            self.row_offset += 1
        if direction == LEFT:
            self.col_offset -= 1
        if direction == RIGHT:
            self.col_offset += 1

    def rotate_piece(self):
        new_indices = []

        self.update_origin()

        origin_row, origin_col = self.origin

        for row, col in self.indices:
            new_indices.append((row - origin_row, col - origin_col))

        count = 0
        for row, col in new_indices:
            new_indices[count] = (col, (-row))
            count += 1

        count = 0
        for row, col in new_indices:
            new_indices[count] = row + origin_row, col + origin_col
            count += 1

        return new_indices

    def update_location(self, direction):

        new_indices = []

        if direction == ROTATE:
            self.indices = self.rotate_piece()
            return

        for index in self.indices:
            if direction == DOWN:
                new_indices.append((index[0] + 1, index[1]))
            if direction == LEFT:
                new_indices.append((index[0], index[1] - 1))
            if direction == RIGHT:
                new_indices.append((index[0], index[1] + 1))

        self.update_offset(direction)
        self.indices = new_indices

    @staticmethod
    def createRandomPiece():
        # create random Piece
        indices = random.choice(SHAPES)
        anchor = (indices[0][0], indices[0][1])
        color = random.choice(NEW_COLORS)
        img_path = os.path.join(f'assets/images/resized_blocks/{color}.png')
        return Piece(indices, anchor, img_path)

