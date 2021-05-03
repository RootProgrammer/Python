import pygame
from pygame.locals import *
from pathlib import *
from resources_and_modules import snake
from resources_and_modules import food
import time

base_directory = Path(__file__).parent.absolute()
object_size = 40  #! dimension of object image. choose a squire sized image.
text_color = (232, 93, 4)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake Game by ZamaaN')

        pygame.mixer.init()
        self.play_background_music('bg_music_1')

        self.window_surface = pygame.display.set_mode((1102, 786))
        self.snake = snake.Snake(self.window_surface, 1)
        self.snake.draw_snake()
        self.food = food.Food(self.window_surface)

        #? Food appears over snake.
        for positon in range(self.snake.snake_size):
            if self.is_hit(self.food.food_x, self.food.food_y, self.snake.snake_x[positon], self.snake.snake_y[positon]):
                self.food.draw_food()

    def is_hit(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + object_size:
            if y1 >= y2 and y1 < y2 + object_size:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 28)
        score = font.render(
            f'Score: {self.snake.snake_size - 1}', True, text_color)

        self.window_surface.blit(score, (995, 11))

    def play_background_music(self, sound_name):
        sound_directory = f'resources_and_modules/resources/{sound_name}.mp3'
        full_ding_directory = base_directory / sound_directory
        pygame.mixer.music.load(full_ding_directory)
        pygame.mixer.music.play(-1)

    def play_sound(self, sound_name):
        sound_directory = f'resources_and_modules/resources/{sound_name}.mp3'
        full_ding_directory = base_directory / sound_directory
        sound = pygame.mixer.Sound(full_ding_directory)
        pygame.mixer.Sound.play(sound)

    def render_background(self):
        background_directory = 'resources_and_modules/resources/background.jpg'
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
        if self.is_hit(self.snake.snake_x[0], self.snake.snake_y[0], self.food.food_x, self.food.food_y):
            self.play_sound('ding')
            self.snake.increase_snake_size()
            self.food.move_food()

        #? Snake eat itself.
        for positon in range(1, self.snake.snake_size):
            if self.is_hit(self.snake.snake_x[0], self.snake.snake_y[0], self.snake.snake_x[positon], self.snake.snake_y[positon]):
                self.play_sound('crash')
                raise 'Game Over!'

        #? Snake hit the boundries of the window
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
        self.snake = snake.Snake(self.window_surface, 1)
        self.food = food.Food(self.window_surface)

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
