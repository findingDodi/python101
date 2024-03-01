import json
import os


def interaction(_todo_list):
    user_action = input('Action: [I]nsert, [D]elete, [E]xit ')
    if user_action == 'I':
        todo = input('Enter todo: ').strip()
        _todo_list.append(todo)
        return True
    elif user_action == 'D':
        # TODO: Index based deletion
        to_delete = input('What would you like to delete? ')
        if to_delete in _todo_list:
            _todo_list.remove(to_delete)
        else:
            print('Try to delete something from the list next time :)')
        return True

    return False


SAVE_FILE = 'todo_list.json'

todo_list = []

if os.path.exists(SAVE_FILE):
    todo_list = json.loads(open(SAVE_FILE).read())

keep_running = True

while keep_running:
    # TODO: Make List-Print pretty (Index based)
    print(todo_list)
    keep_running = interaction(todo_list)

json_file = open(SAVE_FILE, 'w')
json_content = json.dumps(todo_list)
json_file.write(json_content)
json_file.close()
