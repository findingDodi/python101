import time

amount = 99

start_time = time.time()

for i in range(amount, -1, -1):
    if i > 0:
        print(i, "cups of Glühwein on the wall,", i, "cups of Glühwein.")

        if i > 1:
            print("Take one down and pass it around,", (i - 1), "cups of Glühwein on the wall.")
        elif i == 1:
            print("Take one down and pass it around, no more cups of Glühwein on the wall.")

    elif i == 0:
        print("No more cups of Glühwein on the wall, no more cups of Glühwein.")
        print("Go to the store and buy some more, 99 cups of Glühwein on the wall.")

print(time.time() - start_time, "seconds")
