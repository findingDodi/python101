import json
import os


def interaction(_todo_list: list):
    user_action = input('Action: [I]nsert, [D]elete, [E]xit ')
    if user_action == 'I':
        todo = input('Enter todo: ').strip()
        _todo_list.append(todo)
        return True
    elif user_action == 'D':
        index_to_delete = int(input('What would you like to delete? (Enter number) '))
        if index_to_delete < len(_todo_list):
            _todo_list.pop(index_to_delete)
        else:
            print('Try to delete something from the list next time :)')
        return True

    return False


def print_todos(_todo_list):
    for i, todo in enumerate(_todo_list):
        print('[{}] {}'.format(i, todo))


SAVE_FILE = 'todo_list.json'

todo_list = []

if os.path.exists(SAVE_FILE):
    todo_list = json.loads(open(SAVE_FILE).read())

keep_running = True

while keep_running:
    print_todos(todo_list)
    keep_running = interaction(todo_list)

json_file = open(SAVE_FILE, 'w')
json_content = json.dumps(todo_list)
json_file.write(json_content)
json_file.close()
