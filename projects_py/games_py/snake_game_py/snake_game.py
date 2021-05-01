import pygame
from pygame.locals import *
from pathlib import *
import time
import random

base_directory = Path(__file__).parent.absolute()
object_size = 40    #! dimension of object image. choose a squire sized image.
text_color = (232, 93, 4)

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

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake Game by ZamaaN')

        pygame.mixer.init()
        self.play_background_music('bg_music_1')

        self.window_surface = pygame.display.set_mode((1102, 786))
        self.snake = Snake(self.window_surface, 1)
        self.snake.draw_snake()
        self.food = Food(self.window_surface)
        self.food.draw_food()

    def is_eten(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + object_size:
            if y1 >= y2 and y1 < y2 + object_size:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 28)
        score = font.render(f'Score: {self.snake.snake_size - 1}', True, text_color)

        self.window_surface.blit(score,(995, 11))

    def play_background_music(self, sound_name):
        sound_directory = f'resources/{sound_name}.mp3'
        full_ding_directory = base_directory / sound_directory
        pygame.mixer.music.load(full_ding_directory)
        pygame.mixer.music.play()
    
    def play_sound(self, sound_name):
        sound_directory = f'resources/{sound_name}.mp3'
        full_ding_directory = base_directory / sound_directory
        sound = pygame.mixer.Sound(full_ding_directory)
        pygame.mixer.Sound.play(sound)

    def render_background(self):
        background_directory = 'resources/background.jpg'
        full_background_directory = base_directory / background_directory
        background = pygame.image.load(full_background_directory)
        self.window_surface.blit(background, (0, 0))
    
    def play(self):
        self.render_background()
        self.snake.walk_snake()
        self.food.draw_food()
        self.display_score()
        pygame.display.flip()

        #? Snake eat food.
        if self.is_eten(self.snake.snake_x[0], self.snake.snake_y[0], self.food.food_x, self.food.food_y):
            self.play_sound('ding')
            self.snake.increase_snake_size()
            self.food.move_food()

        #? Snake eat itself.
        for positon in range(1, self.snake.snake_size):
            if self.is_eten(self.snake.snake_x[0], self.snake.snake_y[0], self.snake.snake_x[positon], self.snake.snake_y[positon]):
                self.play_sound('crash')

                raise 'Game Over!'

        #? Ssnake hit the boundries of the window
        if not (0 <= self.snake.snake_x[0] <= 1102 and 0 <= self.snake.snake_y[0] <= 786):
            self.play_sound('crash')
            raise "Game Over!"

    def display_game_over(self):
        self.render_background()

        font = pygame.font.SysFont('arial', 28)
        score = font.render(f'Game is Over! Score: {self.snake.snake_size - 1}', True, text_color)
        self.window_surface.blit(score, (200, 300))

        continue_message = font.render('To play again press Enter. To exit press Escape!', True, text_color)
        self.window_surface.blit(continue_message, (200, 350))
        pygame.display.flip()

        pygame.mixer.music.pause()
    
    def reset(self):
        self.snake = Snake(self.window_surface, 1)
        self.food = Food(self.window_surface)
    
    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.display_game_over()
                pause = True
                self.reset()
            
            time.sleep(0.24)


if __name__ == '__main__':
    game = Game()
    game.run()
