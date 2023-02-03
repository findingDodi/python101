# Ladebalken 1a

def get_has_string(amount):
    for i in range(amount):
        print('#', end='')


percentage = 7
rest = 10 - percentage

print("[", end='')
get_has_string(percentage)
print((' ' * rest), end='')
print("]", percentage * 10, "%", end='')
