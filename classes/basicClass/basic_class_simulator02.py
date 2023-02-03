import BasicClass
import random
import string


def get_random_label():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))


def magic_shit():
    print("Begin of Function")
    label = get_random_label()
    instance = BasicClass.BasicClass(label)
    instance.log_time()
    print("Time ist gelogged")
    print(instance.get_info())
    print("Info wurde auf die Konsole ausgegeben")


for i in range(5):
    print("Begin of Loop")
    magic_shit()

print("*" * 10)

instance = None

for i in range(5):
    print("Begin of loop")
    label = get_random_label()
    instance = BasicClass.BasicClass(label)
    instance.log_time()
    print(instance.get_info())

if instance is None:
    print(type(instance))
else:
    print(instance.get_info())

print("End")
