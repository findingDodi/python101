
class TheMazeMaker:

    def __init__(self):
        self.maze = self.get_maze()

    def get_maze(self):
        maze_content = []
        top_bottom_line = '#' * 30
        maze_content.append(list(top_bottom_line))
        other_lines = '#' + ' ' * 28 + '#'
        for i in range(28):
            maze_content.append(list(other_lines))

        maze_content.append(list(top_bottom_line))
        x = 0
        for y in range(len(maze_content)):
            x += 1
            #for x in range(len(maze_content[0])):
            block_upper = x + 1
            block_lower = y + 1
            if block_upper > 0 and block_upper < len(maze_content[0])\
            and block_lower > 0 and block_lower < len(maze_content[0]):
                maze_content[y][x] = '#'

        return maze_content

    def get_maze_from_file_content(self):
        file_handle = open('mazes/maze.txt', 'r')
        file_content = file_handle.readlines()

        return file_content
