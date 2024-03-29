import pygame
import random
import typing

import conf


class GameCore:

    def __init__(self):
        self.screen: typing.Optional[pygame.surface.Surface] = None
        self.screen_width = conf.SCREEN_SIZE[0]
        self.screen_height = conf.SCREEN_SIZE[1]
        self.game_is_running = True
        self.background_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)

    def draw_ants(self):
        ant_amount = int((self.screen_width * self.screen_height) / 2)
        for i in range(ant_amount):
            x = random.randint(0, self.screen_width)
            y = random.randint(0, self.screen_height)
            pygame.draw.rect(self.screen, (255, 255, 255), (x, y, 1, 1))

        '''
        for x in range(self.screen_width):
            for y in range(self.screen_height):
                if random.randint(0, 100) >= 50:
                    self.screen.set_at((x, y), (255, 255, 255))
        '''

    def run_game(self):
        pygame.init()
        pygame.display.set_caption("Ants vs Ants")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        clock = pygame.time.Clock()
        self.game_is_running = True

        while self.game_is_running:
            # limit framespeed to 30fps
            clock.tick(30)
            self.screen.fill((0, 0, 0), self.background_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False

            self.draw_ants()

            # final draw
            pygame.display.flip()
