
def uber_counter():
    memory = 0
    print("Before uber_counter for")
    for i in range(10):
        memory += i
        if memory == 36:
            continue
        print("Before yield")
        yield memory
        print("After yield")


def uber_range(counter):
    for i in range(counter):
        yield i


for count in uber_range(10):
    print(count)

'''
first_uber_number = uber_counter().__next__()
print(first_uber_number)
print("#" * 10)

for count in uber_counter():
    print("Before print count")
    print(count)
    print("After print count")
'''
