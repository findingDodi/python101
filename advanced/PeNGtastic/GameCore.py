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
        self.background_color = (255, 255, 255)

        self.background_image = pygame.image.load("maze.png")
        self.background_image_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)

        self.mouse_color = (200, 100, 50)
        self.mouse_position_x = 20
        self.mouse_position_y = 20
        self.mouse_speed = 1

        self.cursor_position_x = -1
        self.cursor_position_y = -1

    def draw_mouse(self):
        pygame.draw.rect(self.screen, self.mouse_color, (self.mouse_position_x, self.mouse_position_y, 10, 10))

    def set_mouse_position(self, x, y):
        self.mouse_position_x = x
        self.mouse_position_y = y

    def move_mouse(self):
        self.cursor_position_x, self.cursor_position_y = pygame.mouse.get_pos()
        # TODO: find a better way than this:
        print(self.screen.get_at((self.cursor_position_x, self.cursor_position_y)))

        move_x = 0
        move_y = 0

        if self.mouse_position_x < self.cursor_position_x:
            move_x += self.mouse_speed
        elif self.mouse_position_x > self.cursor_position_x:
            move_x -= self.mouse_speed

        if self.mouse_position_y < self.cursor_position_y:
            move_y += self.mouse_speed
        elif self.mouse_position_y > self.cursor_position_y:
            move_y -= self.mouse_speed

        vector_length = math.sqrt(move_x ** 2 + move_y ** 2)
        move_x /= vector_length
        move_y /= vector_length

        self.set_mouse_position(self.mouse_position_x + move_x, self.mouse_position_y + move_y)

    def border_patrol(self):
        if self.mouse_position_x <= 0:
            self.mouse_position_x = 1
        elif self.mouse_position_x > self.screen_width - 20:
            self.mouse_position_x = self.screen_width - 20

        if self.mouse_position_y <= 0:
            self.mouse_position_y = 1
        elif self.mouse_position_y > self.screen_height - 20:
            self.mouse_position_y = self.screen_height - 20

    def run_game(self):

        pygame.init()
        pygame.display.set_caption("PeNGtastic")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        clock = pygame.time.Clock()
        self.game_is_running = True

        while self.game_is_running:
            # limit framespeed to 30fps
            clock.tick(30)
            self.screen.fill(self.background_color, self.background_rect)
            self.screen.blit(self.background_image, self.background_image_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False

            for i in range(5):
                self.draw_mouse()
                self.border_patrol()
                self.move_mouse()

            # final draw
            pygame.display.flip()
