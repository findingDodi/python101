# Ladebalken 2

state = int(int(input("Enter State: "))/10)

if state >= 0:
    i = state
    while i <= 10:
        rest = 10 - state
        ladebalken = (" " * rest).rjust(10, "#")
        print("[", ladebalken, "] ", state * 10, " %", sep='')
        state += 1
        i += 1
