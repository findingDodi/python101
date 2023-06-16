import pygame
import conf
from TheMazeMaker import TheMazeMaker


class TheMaze:

    def __init__(self):
        self.screen = None
        self.game_is_running = True
        self.last_event = None

        self.screen_width = conf.SCREEN_SIZE[0]
        self.screen_height = conf.SCREEN_SIZE[1]

        self.maze_floor_rect = pygame.Rect(20, 20, (self.screen_width - 40), (self.screen_height - 40))
        self.start_point_rect = pygame.Rect(20, 20, 20, 20)
        self.end_point_rect = pygame.Rect((self.screen_width - 40), (self.screen_height - 40), 20, 20)

        self.border_control_top = 20
        self.border_control_bottom = self.screen_height - 40
        self.border_control_left = 20
        self.border_control_right = self.screen_width - 40

        self.runner_position_y = self.border_control_top
        self.runner_position_x = self.border_control_left

        self.old_runner_position_y = self.runner_position_y
        self.old_runner_position_x = self.runner_position_x

        self.color_runner = (255, 255, 255)
        self.color_floor = (50, 50, 50)
        self.color_border = (150, 150, 150)
        self.color_start_point = (250, 50, 200)
        self.color_end_point = (20, 250, 50)

        self.maze_maker = TheMazeMaker()
        self.maze = self.maze_maker.maze
        self.wall_coordinates = self.get_wall_coordinates()

    def draw_runner(self):
        pygame.draw.rect(self.screen, self.color_runner, (self.runner_position_x, self.runner_position_y, 20, 20))

    def draw_maze(self):
        for coordinates in self.wall_coordinates:
            pygame.draw.rect(
                self.screen,
                self.color_border,
                (coordinates[0], coordinates[1], 20, 20)
            )

    def event_control(self, event):
        if event.key == pygame.K_UP:
            self.last_event = pygame.K_UP

        if event.key == pygame.K_DOWN:
            self.last_event = pygame.K_DOWN

        if event.key == pygame.K_LEFT:
            self.last_event = pygame.K_LEFT

        if event.key == pygame.K_RIGHT:
            self.last_event = pygame.K_RIGHT

    def run(self):
        if self.last_event == pygame.K_UP:
            self.runner_position_y -= 20

        if self.last_event == pygame.K_DOWN:
            self.runner_position_y += 20

        if self.last_event == pygame.K_LEFT:
            self.runner_position_x -= 20

        if self.last_event == pygame.K_RIGHT:
            self.runner_position_x += 20

        self.last_event = None

    def get_wall_coordinates(self):
        wall_coordinates = set()
        for y, line in enumerate(self.maze):
            for x, field in enumerate(line):
                if field == '#':
                    wall_position_x = x * 20
                    wall_position_y = y * 20
                    wall_coordinates.add((wall_position_x, wall_position_y))

        return wall_coordinates

    def border_patrol(self):
        if self.runner_position_x < self.border_control_left:
            self.runner_position_x = self.border_control_left
        elif self.runner_position_x >= self.border_control_right:
            self.runner_position_x = self.border_control_right

        if self.runner_position_y < self.border_control_top:
            self.runner_position_y = self.border_control_top
        elif self.runner_position_y >= self.border_control_bottom:
            self.runner_position_y = self.border_control_bottom

    def maze_patrol(self):
        if (self.runner_position_x, self.runner_position_y) in self.wall_coordinates:
            self.runner_position_x, self.runner_position_y = self.old_runner_position_x, self.old_runner_position_y
        else:
            self.old_runner_position_x, self.old_runner_position_y = self.runner_position_x, self.runner_position_y

    def run_maze(self):
        pygame.init()
        pygame.display.set_caption("Maze Runner")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        self.game_is_running = True

        while self.game_is_running:
            self.screen.fill(self.color_floor, self.maze_floor_rect)
            self.draw_maze()

            self.screen.fill(self.color_start_point, self.start_point_rect)
            self.screen.fill(self.color_end_point, self.end_point_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False
                    else:
                        self.event_control(event)
                        self.run()
                        self.border_patrol()
                        self.maze_patrol()

            self.draw_runner()
            pygame.display.flip()


myze = TheMaze()
myze.run_maze()
