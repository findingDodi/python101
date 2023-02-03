import random
import time

all_ids = set()
random_id = 1


def get_id():
    global random_id
    while random_id in all_ids:
        #random_id = random.randrange(99999)
        random_id += 1

    return random_id


keep_running = True

while keep_running:
    start_time = time.time()
    new_id = get_id()
    print(time.time() - start_time, len(all_ids))
    all_ids.add(new_id)
    if len(all_ids) >= 99999:
        keep_running = False
