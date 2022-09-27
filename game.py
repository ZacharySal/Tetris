import pygame
import os

from const import *
from square import *
from board import Board


class Game:

    def __init__(self):
        pass

    def show_bg(self, surface):
        for col in range(COLS):
            for row in range(ROWS):
                if col == 0 or col == COLS - 1:
                    color = (130, 0, 255)
                else:
                    color = (0, 0, 0)
                rect = (col * SQUARE_WIDTH, row * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, board, surface):
        for piece in board.pieces:
            for row, col in piece.indices:
                if board.squares[row][col].occupied:
                    # print(index)
                    rect = (col * SQUARE_WIDTH, row * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT)
                    pygame.draw.rect(surface, piece.color, rect)









