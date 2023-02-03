import random
import os
import time

# Emoji Fun
'''
TWIG = '🎄'
BALL = '🎊'
TRIBE = '🪵🪵🪵'
BACKGROUND = '🖤'
'''
TOP = '*'
TWIG = '^'
BALL = 'o'
TRIBE = '|||'
BACKGROUND = ' '


def get_tree_package(width):
    tree_bottom_width = width
    all_tree_levels = []
    counter = 1

    while counter <= tree_bottom_width:
        if counter == 1:
            current_tree_level = TOP
        else:
            current_tree_level = counter * TWIG
            random_ball_number = random.randrange(counter)
            '''
            current_tree_level\
                = current_tree_level[:random_ball_number]\
                + BALL\
                + current_tree_level[random_ball_number + 1:]
            
            current_tree_level = '{}{}{}'.format(
                current_tree_level[:random_ball_number], 
                BALL, 
                current_tree_level[random_ball_number + 1:]
            )
            '''
            current_tree_level = list(current_tree_level)
            current_tree_level[random_ball_number] = BALL
            current_tree_level = ''.join(current_tree_level)

        current_tree_level = current_tree_level.center(tree_bottom_width, BACKGROUND)
        all_tree_levels.append(current_tree_level)
        counter += 2

    all_tree_levels.append(TRIBE.center(tree_bottom_width, BACKGROUND))
    all_tree_levels.append(TRIBE.center(tree_bottom_width, BACKGROUND))

    return all_tree_levels


def build_xmas_tree(tree_levels):
    for tree_level in tree_levels:
        print(tree_level)


if __name__ == '__main__':
    timing = 0
    start = time.time()
    while timing < 15:
        bottom_width = 19
        tree_package = get_tree_package(bottom_width)
        build_xmas_tree(tree_package)
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        end = time.time()
        timing = end - start
