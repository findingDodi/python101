
inputNumber = input("Enter MAX: ")
maxNumber = int(inputNumber)

if maxNumber >= 1:
    for i in range(maxNumber):
        print("#" * (i + 1))
else:
    print("Wrong Number")

print("*" * 10)

if int(inputNumber):
    for i in range(int(inputNumber)):
        print("#" * (i + 1))
else:
    print("Wrong Number")
