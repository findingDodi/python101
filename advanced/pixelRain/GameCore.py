import pygame

from PixelBox import PixelBox
import conf


class GameCore:

    def __init__(self):
        self.screen = None
        self.screen_width = conf.SCREEN_SIZE[0]
        self.screen_height = conf.SCREEN_SIZE[1]
        self.game_is_running = True
        self.spawn_interval = 1000
        self.spawn_time = pygame.time.get_ticks()

        self.background_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.background_color = (0, 0, 0)

        self.pixel_boxes = []

    def draw_pixel_box(self, pixel_box):
        pygame.draw.rect(self.screen, pixel_box.pixel_box_color, (pixel_box.pixel_box_pos_x, pixel_box.pixel_box_pos_y, 20, 20))

    def move_pixel_box(self):
        for box in self.pixel_boxes:
            box.fall()
            self.draw_pixel_box(box)

    def spawn_pixel_box(self):
        pixel_box = PixelBox(pygame.mouse.get_pos()[0], conf.BOX_COLOR)
        self.pixel_boxes.append(pixel_box)
        self.draw_pixel_box(pixel_box)

    def border_patrol(self):
        for box in self.pixel_boxes:
            if box.pixel_box_pos_y > self.screen_height:
                self.pixel_boxes.remove(box)

    def run_game(self):
        pygame.init()
        pygame.display.set_caption("Pixel Rain")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        self.screen.fill(self.background_color, self.background_rect)
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

            current_time = pygame.time.get_ticks()
            if current_time > self.spawn_time:
                self.spawn_pixel_box()
                self.spawn_time += self.spawn_interval

            self.move_pixel_box()
            self.border_patrol()
            print(len(self.pixel_boxes))

            # final draw
            pygame.display.flip()
