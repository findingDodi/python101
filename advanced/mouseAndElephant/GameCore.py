import pygame
import math

import conf


class GameCore:

    def __init__(self):
        self.screen = None
        self.screen_width = conf.SCREEN_SIZE[0]
        self.screen_height = conf.SCREEN_SIZE[1]
        self.game_is_running = True
        self.background_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)

        self.elephant_position_x = self.screen_width / 2
        self.elephant_position_y = self.screen_height / 2
        self.elephant_speed = 1
        self.elephant_color = (190, 190, 190)

        self.mouse_pos_x = -1
        self.mouse_pos_y = -1

    def draw_elephant(self):
        pygame.draw.rect(self.screen, self.elephant_color, (self.elephant_position_x, self.elephant_position_y, 20, 20))

    def set_elephant_position(self, x, y):
        self.elephant_position_x = x
        self.elephant_position_y = y

    def move_elephant(self):
        self.mouse_pos_x, self.mouse_pos_y = pygame.mouse.get_pos()

        move_x = 0
        move_y = 0

        if self.elephant_position_x < self.mouse_pos_x:
            move_x -= self.elephant_speed
        elif self.elephant_position_x > self.mouse_pos_x:
            move_x += self.elephant_speed

        if self.elephant_position_y < self.mouse_pos_y:
            move_y -= self.elephant_speed
        elif self.elephant_position_y > self.mouse_pos_y:
            move_y += self.elephant_speed

        vector_length = math.sqrt(move_x ** 2 + move_y ** 2)
        move_x /= vector_length
        move_y /= vector_length

        self.set_elephant_position(self.elephant_position_x + move_x, self.elephant_position_y + move_y)

    def border_patrol(self):
        if self.elephant_position_x < 20:
            self.elephant_position_x = 20
        elif self.elephant_position_x > self.screen_width - 40:
            self.elephant_position_x = self.screen_width - 40

        if self.elephant_position_y < 20:
            self.elephant_position_y = 20
        elif self.elephant_position_y > self.screen_height - 40:
            self.elephant_position_y = self.screen_height - 40

    def run_game(self):

        pygame.init()
        pygame.display.set_caption("Mouse and Elephant")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        clock = pygame.time.Clock()
        self.game_is_running = True

        while self.game_is_running:
            # limit framespeed to 30fps
            clock.tick(30)
            self.screen.fill((55, 55, 55), self.background_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False

            for i in range(5):
                self.move_elephant()
                self.border_patrol()
                self.draw_elephant()

            # final draw
            pygame.display.flip()
