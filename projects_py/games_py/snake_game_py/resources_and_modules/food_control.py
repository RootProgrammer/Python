import pygame
from pathlib import *
import random

base_directory = Path(__file__).parent.absolute()
object_size = 40  # ! dimension of object image. choose a squire sized image.

class Food:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.food_directory = 'resources/apple.jpg'
        self.full_food_directory = base_directory / self.food_directory
        self.food = pygame.image.load(self.full_food_directory).convert()
        self.food_x = object_size * 3
        self.food_y = object_size * 3

    def draw_food(self):
        self.parent_screen.blit(self.food, (self.food_x, self.food_y))
        pygame.display.flip()

    def move_food(self):
        self.food_x = random.randint(0, 26) * object_size
        self.food_y = random.randint(0, 18) * object_size
