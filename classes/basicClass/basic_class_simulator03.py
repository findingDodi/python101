import BasicClass
import random
import string
import time


def get_random_label(amount):
    # return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    output = ''
    letters_numbers = string.ascii_uppercase + string.digits
    for _ in range(amount):
        output += random.choice(letters_numbers)

    return output


new_array = []

start_time = time.time()
total_time = 0
timing = 0

for i in range(5):
    label = get_random_label(5)
    inner_start_time = time.time()
    instance = BasicClass.BasicClass(label)
    instance.log_time()
    inner_end_time = time.time()
    timing += inner_end_time - inner_start_time
    total_time += instance.logged_time - start_time
    print(instance.get_info())
    new_array.append(instance)


end_time = time.time()
all_time = end_time - start_time
print("Zeit für den kompletten Loop:", all_time)
print("Zeit für der Loop-Schritte:", total_time)
print("Netto-Zeit:", timing)
