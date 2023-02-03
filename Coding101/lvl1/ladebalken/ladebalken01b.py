# Ladebalken 1b

percentage = 3
rest = 10 - percentage
ladebalken = (" " * rest).rjust(10, "#")
print("[", ladebalken, "] ", percentage * 10, " %", sep='')
