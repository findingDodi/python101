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
        self.background_color = (0, 0, 0)

        self.mouse_pressed = False
        self.mouse_pos_x = -1
        self.mouse_pos_y = -1

        self.pencil_color = (255, 255, 255)
        self.brush_size = 5

    def clean(self):
        x, y = pygame.mouse.get_pos()
        if x != self.mouse_pos_x or y != self.mouse_pos_y:
            if self.mouse_pos_x >= 0 and self.background_rect.collidepoint(x, y):
                pygame.draw.circle(self.screen, self.pencil_color, (self.mouse_pos_x, self.mouse_pos_y), self.brush_size)
            self.mouse_pos_x = x
            self.mouse_pos_y = y

    def run_game(self):

        pygame.init()
        pygame.display.set_caption("Mouse Cleaner")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        self.screen.fill(self.background_color, self.background_rect)
        clock = pygame.time.Clock()
        self.game_is_running = True

        while self.game_is_running:
            # limit framespeed to 30fps
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False

            self.clean()

            # final draw
            pygame.display.flip()
