import time

import pygame
import os

from const import *
from square import *
from board import Board

class Game:
    def __init__(self, board):
        self.board = board

    def render_text(self, surface, text, size, color, x_offset, y_offset):
        font = pygame.font.SysFont('Fixedsys', size)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH - x_offset, HEIGHT - y_offset)
        surface.blit(text, text_rect)
    def show_game_info(self, record, surface):

        self.render_text(surface, f'Score: {self.board.score}', 40, (255, 255, 255), 150, 900)
        self.render_text(surface, f'Top: {record}', 40, (255, 255, 255), 150, 860)
        self.render_text(surface, f'Lines: {self.board.completed_rows}', 35, (255, 255, 255), 150, 400)
        self.render_text(surface, f'Level: {self.board.level}', 35, (255, 255, 255), 150, 460)

        for row, col in self.board.next_piece.indices:
            # piece = self.board.next_piece
            # rect = (col * (140 // 4) + 380, row * (180 // 4) + 700, (140 // 4), (180 // 4))
            # pygame.draw.rect(surface, piece.color, rect)

            img = pygame.image.load(self.board.next_piece.img_path).convert_alpha()
            img_center = col * SQUARE_WIDTH + SQUARE_WIDTH // 2 + 650, row * SQUARE_HEIGHT + SQUARE_HEIGHT // 2 + 330
            texture_rect = img.get_rect(center=img_center)
            surface.blit(img, texture_rect)

    def show_start_screen(self, surface):
        self.render_text(surface, 'TETRIS', 80, (42, 200, 150), WIDTH // 2, 700)
        self.render_text(surface, 'Press Space to Start!', 40, (255, 80, 110), WIDTH // 2, 550)
        self.render_text(surface, 'A to move left', 40, (255, 255, 108), WIDTH // 2, 400)
        self.render_text(surface, 'D to move right', 40, (255, 255, 108), WIDTH // 2, 350)
        self.render_text(surface, 'S to move down', 40, (255, 255, 108), WIDTH // 2, 300)
        self.render_text(surface, 'R to rotate piece', 40, (255, 255, 108), WIDTH // 2, 250)
        self.render_text(surface, 'Space to auto-complete piece', 40, (255, 255, 108), WIDTH // 2, 200)

    def show_border(self, surface):
        for col in range(COLS):
            for row in range(-1, 21, 1):
                if col == 0 or col == COLS - 1 or row == -1 or row == 20:
                    img = pygame.image.load(os.path.join("assets/images/resized_blocks/blue.png"))
                    img_center = col * SQUARE_WIDTH + SQUARE_WIDTH // 2 + 200, row * SQUARE_HEIGHT + SQUARE_HEIGHT // 2 + 100
                    # color = (127, 127, 127)
                    # rect = (col * SQUARE_WIDTH, row * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT)
                    texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, texture_rect)
                    # pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for piece in self.board.pieces:
            for row, col in piece.indices:
                img = pygame.image.load(piece.img_path).convert_alpha()
                img_center = col * SQUARE_WIDTH + SQUARE_WIDTH // 2 + 200, row * SQUARE_HEIGHT + SQUARE_HEIGHT // 2 + 100
                texture_rect = img.get_rect(center=img_center)
                surface.blit(img, texture_rect)
                # rect = (col * SQUARE_WIDTH, row * SQUARE_HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT)
                # pygame.draw.rect(surface, piece.color, rect)

    def show_piece_trace(self, surface):
        for ghost_row, ghost_col in self.board.active_piece.trace:
            valid = True
            for piece_row, piece_col in self.board.active_piece.indices:
                if ghost_row == piece_row and ghost_col == piece_col:
                    valid = False

            if valid:
                rect = (ghost_col * SQUARE_WIDTH + 200, ghost_row * SQUARE_HEIGHT + 100, SQUARE_WIDTH, SQUARE_HEIGHT)
                pygame.draw.rect(surface, (255, 255, 255), rect)

    def show_end_screen(self, surface):
        for row in range(ROWS):
            for col in range(1, 15, 1):
                if row % 2 == 0:
                    img = pygame.image.load(os.path.join("assets/images/resized_blocks/orange.png"))
                else:
                    img = pygame.image.load(os.path.join("assets/images/resized_blocks/red.png"))

                img_center = col * SQUARE_WIDTH + SQUARE_WIDTH // 2 + 200, row * SQUARE_HEIGHT + SQUARE_HEIGHT // 2 + 100
                texture_rect = img.get_rect(center=img_center)
                surface.blit(img, texture_rect)

                self.show_border(surface)
                self.render_text(surface, 'Game over!', 40, (255, 80, 110), 150, 670)
                self.render_text(surface, f'Score: {self.board.score}', 30, (255, 255, 255), 150, 550)
                self.render_text(surface, f'Lines: {self.board.completed_rows}', 30, (255, 255, 255), 150, 490)
                self.render_text(surface, 'Press Space to Play Again!', 20, (255, 80, 110), 150, 370)

                pygame.display.update()

        pygame.event.clear()








