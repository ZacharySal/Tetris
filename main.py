import sys
import time

import pygame

from const import *
from board import Board
from game import Game

# TODO:
# Add wall kicks, improve rotation
# Find suitable colors for UI/Pieces and new Fonts

class Main:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Tetris')

        self.board = Board()
        self.game = Game(self.board)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.record = self.get_record()

    def mainloop(self, replay=False):
        if not replay:
            if self.start_screen():
                self.game_loop()
        else:
            self.game_loop()

    def start_screen(self):
        self.screen.fill(BG_COLOR)
        self.game.show_start_screen(self.screen)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True

    def game_over_screen(self):
        self.screen.fill(BG_COLOR)
        self.game.show_end_screen(self.screen)
        self.set_record(self.board.score)
        self.record = self.get_record()
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # create new game
                        self.board = Board()
                        self.game = Game(self.board)
                        self.mainloop(True)

    def game_loop(self):
        game = self.game
        board = self.board
        screen = self.screen
        clock = self.clock
        board.add_piece()

        move_map = {
            pygame.K_s: DOWN,
            pygame.K_a: LEFT,
            pygame.K_d: RIGHT,
        }

        pygame.time.set_timer(DROP, LEVEL_SPEED.get(board.level))
        start_time = pygame.time.get_ticks()

        while not board.game_over:

            screen.fill(BG_COLOR)
            game.show_pieces(screen)
            game.show_border(screen)
            game.show_piece_trace(screen)
            game.show_game_info(self.record, screen)

            if board.level_up:
                print(f'Level: {board.level}')
                print(f'Corresponding drop speed in ms: {LEVEL_SPEED.get(board.level)}')
                pygame.time.set_timer(DROP, LEVEL_SPEED.get(board.level))
                board.level_up = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == DROP:
                    board.update_piece(DOWN)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        board.fast_drop()
                    if event.key == pygame.K_r:
                        board.update_piece(ROTATE)

            pressed = pygame.key.get_pressed()
            move = [move_map[key] for key in move_map if pressed[key]]

            if move and start_time + 90 < pygame.time.get_ticks():
                board.update_piece(move[0])
                start_time = pygame.time.get_ticks()

            pygame.display.update()
            clock.tick(FPS)

        self.set_record(board.score)
        self.game_over_screen()

    def get_record(self):
        try:
            with open('record') as file:
                return file.readline()
        except FileNotFoundError:
            with open('record', 'w') as file:
                file.write('0')
    def set_record(self, score):
        rec = max(int(self.record), score)
        with open('record', 'w') as file:
            file.write(str(rec))


main = Main()
main.mainloop()






