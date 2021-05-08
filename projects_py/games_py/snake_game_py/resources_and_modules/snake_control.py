import pygame
from pathlib import *

base_directory = Path(__file__).parent.absolute()
object_size = 40  # ! dimension of object image. choose a squire sized image.

class Snake:
    def __init__(self, parent_screen, snake_size):
        self.parent_screen = parent_screen
        self.snake_directory = 'resources/block.jpg'
        self.full_snake_directory = base_directory / self.snake_directory
        self.snake = pygame.image.load(self.full_snake_directory).convert()

        self.direction = 'right'
        self.snake_size = snake_size
        self.snake_x = [object_size]*snake_size
        self.snake_y = [object_size]*snake_size

    def draw_snake(self):
        for size in range(self.snake_size):
            self.parent_screen.blit(self.snake, (self.snake_x[size], self.snake_y[size]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk_snake(self):
        for position in range(self.snake_size-1, 0, -1):
            self.snake_x[position] = self.snake_x[position-1]
            self.snake_y[position] = self.snake_y[position-1]

        if self.direction == 'left':
            self.snake_x[0] -= object_size
        elif self.direction == 'right':
            self.snake_x[0] += object_size
        elif self.direction == 'up':
            self.snake_y[0] -= object_size
        elif self.direction == 'down':
            self.snake_y[0] += object_size

        self.draw_snake()

    def increase_snake_size(self):
        self.snake_size += 1
        self.snake_x.append(-1)
        self.snake_y.append(-1)
