import pygame

import conf


class GameCore:

    def __init__(self):
        self.screen = None
        self.screen_width = conf.SCREEN_SIZE[0]
        self.screen_height = conf.SCREEN_SIZE[1]
        self.game_is_running = True
        self.background_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)

        self.cat_position_x = self.screen_width / 2
        self.cat_position_y = self.screen_height / 2
        self.cat_speed = 1
        self.cat_color = (245, 101, 44)

        self.mouse_pos_x = -1
        self.mouse_pos_y = -1

    def draw_cat(self):
        pygame.draw.rect(self.screen, self.cat_color, (self.cat_position_x, self.cat_position_y, 20, 20))

    def sit_cat_position(self, x, y):
        self.cat_position_x = x
        self.cat_position_y = y

    def move_cat(self):
        self.mouse_pos_x, self.mouse_pos_y = pygame.mouse.get_pos()

        move_x = 0
        move_y = 0

        if self.cat_position_x < self.mouse_pos_x:
            move_x += self.cat_speed
        elif self.cat_position_x > self.mouse_pos_x:
            move_x -= self.cat_speed

        if self.cat_position_y < self.mouse_pos_y:
            move_y += self.cat_speed
        elif self.cat_position_y > self.mouse_pos_y:
            move_y -= self.cat_speed

        self.sit_cat_position(self.cat_position_x + move_x, self.cat_position_y + move_y)

    def border_patrol(self):
        if self.cat_position_x < 0:
            self.cat_position_x = 0
        elif self.cat_position_x > self.screen_width - 20:
            self.cat_position_x = self.screen_width - 20

        if self.cat_position_y < 0:
            self.cat_position_y = 0
        elif self.cat_position_y > self.screen_height - 20:
            self.cat_position_y = self.screen_height - 20

    def run_game(self):

        pygame.init()
        pygame.display.set_caption("Cat and Mouse")
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
                self.move_cat()
                self.border_patrol()
                self.draw_cat()

            # final draw
            pygame.display.flip()
