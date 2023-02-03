# for-Schleife bis 10
# jede Zahl im Terminal
# immer einen weiter nach rechts eingerückt (mit Space)


print('First try')

counter = 0
output = ''

for i in range(10):
    output += (' ' * counter)
    output += str(i)
    print(output)

    counter += 1
    output = ''


print('Second try')

counter2 = 0

for i in range(10):
    print(' ' * counter2, i)
    counter2 += 1


print('Third try')

for i in range(10):
    print(' ' * i, i)

