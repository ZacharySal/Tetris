import pygame
import os

from const import *
from square import *
from board import Board


# update the top left of where we are rending the board, move it 100 pixels to right or so


class Game:
    def __init__(self):
        pass

    def show_game_info(self, score, surface):
        font = pygame.font.Font('freesansbold.ttf', 70)
        text = font.render('Tetris', True, (255, 80, 110))
        text_rect = text.get_rect()
        text_rect.center = (WIDTH + 150, HEIGHT - 670)
        surface.blit(text, text_rect)

        # score text
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render('Score', True, (42, 200, 150))
        text_rect = text.get_rect()
        text_rect.center = (WIDTH + 150, HEIGHT - 550)
        surface.blit(text, text_rect)

        font = pygame.font.Font('freesansbold.ttf', 35)
        score = str(score)
        text = font.render(score, True, (255, 165, 0))
        text_rect = text.get_rect()
        text_rect.center = (WIDTH + 150, HEIGHT - 480)
        surface.blit(text, text_rect)
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
                # print(index)
                rect = (col * SQUARE_WIDTH, row * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT)
                pygame.draw.rect(surface, piece.color, rect)









