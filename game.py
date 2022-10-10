import time

import pygame
import os

from const import *
from square import *
from board import Board

class Game:
    def __init__(self):
        pass

    def render_text(self,surface, text, size, color, x_offset, y_offset):
        font = pygame.font.Font('freesansbold.ttf', size)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH - x_offset, HEIGHT - y_offset)
        surface.blit(text, text_rect)
    def show_game_info(self, board, score, record, surface):

        self.render_text(surface, 'Tetris', 70, (255, 80, 110), 150, 670)
        self.render_text(surface, 'Score', 40, (42, 200, 150), 150, 550)
        self.render_text(surface, str(score), 35, (255, 165, 0), 150, 500)
        self.render_text(surface, 'High Score', 40, (42, 200, 115), 150, 430)
        self.render_text(surface, str(record), 35, (255, 165, 0), 150, 380)
        self.render_text(surface, f'Lines: {board.completed_rows}', 35, (255, 255, 255), 150, 280)
        self.render_text(surface, f'Level: {board.level}', 35, (255, 255, 255), 150, 220)

        for row, col in board.next_piece.indices:
            piece = board.next_piece
            rect = (col * (140 // 4) + 380, row * (180 // 4) + 700, (140 // 4), (180 // 4))
            pygame.draw.rect(surface, piece.color, rect)

    def show_start_screen(self, surface):
        self.render_text(surface, 'TETRIS', 80, (42, 200, 150), WIDTH // 2, 700)
        self.render_text(surface, 'Press Space to Start!', 40, (255, 80, 110), WIDTH // 2, 550)
        self.render_text(surface, 'A to move left', 40, (255, 255, 108), WIDTH // 2, 400)
        self.render_text(surface, 'D to move right', 40, (255, 255, 108), WIDTH // 2, 350)
        self.render_text(surface, 'S to move down', 40, (255, 255, 108), WIDTH // 2, 300)
        self.render_text(surface, 'R to rotate piece', 40, (255, 255, 108), WIDTH // 2, 250)
        self.render_text(surface, 'Space to auto-complete piece', 40, (255, 255, 108), WIDTH // 2, 200)

    def show_end_screen_info(self, surface, score):
        self.render_text(surface, 'Game over!', 50, (255, 80, 110), 150, 670)
        self.render_text(surface, f'Score: {score}', 40, (42, 200, 150), 150, 550)
        self.render_text(surface, 'Press Space to Play Again!', 20, (42, 200, 115), 150, 430)

    def show_bg(self, surface):
        for col in range(COLS):
            for row in range(ROWS):
                if col == 0 or col == COLS - 1:
                    color = (127, 127, 127)
                    rect = (col * SQUARE_WIDTH, row * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT)
                    pygame.draw.rect(surface, color, rect)

    def show_pieces(self, board, surface):
        for piece in board.pieces:
            for row, col in piece.indices:
                rect = (col * SQUARE_WIDTH, row * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT)
                pygame.draw.rect(surface, piece.color, rect)

    def show_piece_trace(self, board, surface):
        for ghost_row, ghost_col in board.active_piece.trace:
            valid = True
            for piece_row, piece_col in board.active_piece.indices:
                if ghost_row == piece_row and ghost_col == piece_col:
                    # don't show pieces overlapping current piece
                    valid = False

            if valid:
                rect = (ghost_col * SQUARE_WIDTH, ghost_row * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT)
                pygame.draw.rect(surface, (255, 255, 255), rect)

    def show_end_screen(self, board, score, record, surface):
        for row in range(ROWS):
            for col in range(1, 15, 1):
                if row % 2 == 0:
                    color = (100, 100, 100)
                else:
                    color = (200, 200, 200)

                rect = (col * SQUARE_WIDTH, row * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT)
                pygame.draw.rect(surface, color, rect)

                self.show_bg(surface)
                self.show_end_screen_info(surface, score)
                pygame.display.update()
                pygame.time.delay(4)

        pygame.event.clear()








