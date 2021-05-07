'''
-------
MODULES
-------
'''
import pygame
from pygame.locals import *
from tic_tac_toe_resources import control_board

'''
---------
CONSTANTS
---------
'''
width = height = 600
board_rows = 3
board_columns = 3
box_size = width // board_columns
screen_color = (28, 170, 156)

class Game_TicTacToe:
    def __init__(self):
        pygame.init()
        self.board = control_board.Board()
        self.board.draw_board()
        self.player = 1
    
    def restart(self):
        self.board.screen.fill(screen_color)
        self.board.draw_board()

        self.player = 1

        for row in range(board_rows):
            for column in range(board_columns):
                self.board.console_board[row][column] = 0
        
    def run(self):
        running = True
        game_over = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_RETURN:
                        self.restart()
                        game_over = False

                elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]
                    clicked_row = int(mouse_y // box_size)
                    clicked_column = int(mouse_x // box_size)

                    if self.board.is_box_available(clicked_row, clicked_column):
                        self.board.mark_box(clicked_row, clicked_column, self.player)
                        if self.board.check_win(self.player):
                            game_over = True
                        
                        self.player = self.player % 2 + 1
                        self.board.draw_figures()
                
                elif event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

if __name__ == '__main__':
    game = Game_TicTacToe()
    game.run()
