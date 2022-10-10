import sys
import time

import pygame

from const import *
from board import Board
from game import Game

# TODO


class Main:

    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Tetris')


        self.board = Board()
        self.game = Game()
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
        self.game.show_end_screen(self.board, self.board.score, self.record, self.screen)
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
                        self.mainloop(True)

    def game_loop(self):
        game = self.game
        board = self.board
        screen = self.screen
        clock = self.clock
        board.add_piece()

        pygame.time.set_timer(DROP, LEVEL_SPEED.get(board.level))

        while not board.game_over:

            screen.fill(BG_COLOR)
            game.show_bg(screen)
            game.show_pieces(board, screen)
            game.show_piece_trace(board, screen)
            game.show_game_info(board, board.score, self.record, screen)

            if board.level_up:
                pygame.time.set_timer(DROP, LEVEL_SPEED.get(board.level))
                board.level_up = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == DROP:
                    board.update_piece(DOWN)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        direction = DOWN
                    elif event.key == pygame.K_a:
                        direction = LEFT
                    elif event.key == pygame.K_d:
                        direction = RIGHT
                    elif event.key == pygame.K_r:
                        direction = ROTATE
                    elif event.key == pygame.K_SPACE:
                        board.fast_drop()
                        break
                    else:
                        break

                    board.update_piece(direction)

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






