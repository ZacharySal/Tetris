import sys
import time

import pygame

from const import *
from board import Board
from game import Game

# TODO
# check for row completion
# add anchor identifier for each piece

# CHANGE SQUARE TO OCCUPIED WHEN TAKEN BY A PIECE TO ALLOW FOR EASIER CHECKING OF OTHER THINGS


class Main:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tetris')

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = Board()
        self.game = Game()
        self.clock = pygame.time.Clock()

    def mainloop(self):

        game = self.game
        board = self.board
        screen = self.screen
        clock = self.clock

        color_index = 0
        counter = 0
        acceleration = 10
        board.add_piece()

        while True:
            game.show_bg(screen)
            game.show_pieces(board, screen)

            if board.game_over:
                # print('MAIN')
                pygame.quit()
                sys.exit()

            # add acceleration to active piece past y game ticks
            if counter % 30 == 0 and counter != 0:
                pass
                # board.update_piece(-1)
                # print('accelerating')

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        direction = DOWN
                    elif event.key == pygame.K_a:
                        direction = LEFT
                    elif event.key == pygame.K_d:
                        direction = RIGHT
                    elif event.key == pygame.K_r:
                        direction = ROTATE
                    else:
                        break

                    board.update_piece(direction)

            counter += 1
            pygame.display.update()
            clock.tick(20)


main = Main()
main.mainloop()





