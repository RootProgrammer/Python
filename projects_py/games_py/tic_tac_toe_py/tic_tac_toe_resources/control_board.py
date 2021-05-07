'''
-------
MODULES
-------
'''
import pygame
from pathlib import *
import numpy as np

'''
---------
CONSTANTS
---------
'''
base_directory = Path(__file__).parent.absolute()
icon_path = 'images/tic_tac_toe.ico'
full_icon_path = base_directory / icon_path
width = height = 600
line_width = 14
board_rows = 3
board_columns = 3
box_size = width // board_columns
circle_radius = box_size // 3
cross_box_space = box_size // 4
circle_width = cross_width = 24
screen_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (1, 111, 124)
cross_color = (65, 65, 65)

class Board:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.icon = pygame.image.load(full_icon_path)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption('Tic Tac Toe by ZamaaN')
        self.screen.fill(screen_color)
        self.console_board = np.zeros((board_rows, board_columns))

    def draw_board(self):
        #? first horizontal line
        pygame.draw.line(self.screen, line_color, (11, box_size), (width - 11, box_size), line_width)

        #? second horizontal line
        pygame.draw.line(self.screen, line_color, (11, 2 * box_size), (width - 11, 2 * box_size), line_width)

        #? first vertical line
        pygame.draw.line(self.screen, line_color, (box_size, 11), (box_size, height - 11), line_width)

        #? second vertical line
        pygame.draw.line(self.screen, line_color, (2 * box_size, 11),
                         (2 * box_size, height - 11), line_width)

    def draw_figures(self):
        for row in range(board_rows):
            for column in range(board_columns):
                if self.console_board[row][column] == 1:
                    pygame.draw.circle(self.screen, circle_color, (int(column * box_size + box_size // 2), int(row * box_size + box_size // 2)), circle_radius, circle_width)

                elif self.console_board[row][column] == 2:
                    pygame.draw.line(self.screen, cross_color, (column * box_size + cross_box_space, row * box_size + box_size - cross_box_space), (column *box_size + box_size - cross_box_space, row * box_size + cross_box_space), cross_width)

                    pygame.draw.line(self.screen, cross_color, (column * box_size + cross_box_space, row * box_size + cross_box_space), (column *box_size + box_size - cross_box_space, row * box_size + box_size - cross_box_space), cross_width)

    def mark_box(self, row, column, player):
        self.console_board[row][column] = player

    def is_box_available(self, row, column):
        return self.console_board[row][column] == 0

    def is_board_full(self):
        for row in range(board_rows):
            for column in range(board_columns):
                if self.console_board[row][column] == 0:
                    return False
        
        return True

    def draw_vertical_winning_line(self, column, player):
        position_x = column * box_size + box_size // 2

        if player == 1:
            vertical_winning_line_color = circle_color
        elif player == 2:
            vertical_winning_line_color = cross_color

        pygame.draw.line(self.screen, vertical_winning_line_color, (position_x, 14), (position_x, height - 14), 14)

    def draw_horizontal_winning_line(self, row, player):
        position_y = row * box_size + box_size // 2

        if player == 1:
            horizontal_winning_line_color = circle_color
        elif player == 2:
            horizontal_winning_line_color = cross_color

        pygame.draw.line(self.screen, horizontal_winning_line_color, (14, position_y), (width - 14, position_y), 14)

    def draw_ascending_diagonal_winning_line(self, player):
        if player == 1:
            ascending_diagonal_winning_line_color = circle_color
        elif player == 2:
            ascending_diagonal_winning_line_color = cross_color

        pygame.draw.line(self.screen, ascending_diagonal_winning_line_color, (14, height - 14), (width - 14, 14), 14)

    def draw_descending_diagonal_winning_line(self, player):
        if player == 1:
            descending_diagonal_winning_line_color = circle_color
        elif player == 2:
            descending_diagonal_winning_line_color = cross_color

        pygame.draw.line(self.screen, descending_diagonal_winning_line_color, (14, 14), (width - 14, height - 14), 14)

    def check_win(self, player):
        #? vertical win check
        for column in range(board_columns):
            if self.console_board[0][column] == player and self.console_board[1][column] == player and self.console_board[2][column] == player:
                self.draw_vertical_winning_line(column, player)
                return True

        #? horizontal win check
        for row in range(board_rows):
            if self.console_board[row][0] == player and self.console_board[row][1] == player and self.console_board[row][2] == player:
                self.draw_horizontal_winning_line(row, player)
                return True

        #? ascending diagonal win check
        if self.console_board[2][0] == player and self.console_board[1][1] == player and self.console_board[0][2] == player:
            self.draw_ascending_diagonal_winning_line(player)
            return True

        #? descending diagonal win check
        if self.console_board[0][0] == player and self.console_board[1][1] == player and self.console_board[2][2] == player:
            self.draw_descending_diagonal_winning_line(player)
            return True

        return False
