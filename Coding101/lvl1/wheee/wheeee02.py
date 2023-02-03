inputNumber = int(input("Enter MAX: "))


if inputNumber >= 1:
    for i in range(inputNumber):
        print("#" * (i+1))
        
    for i in range(inputNumber-1, 0, -1):
        print("#" * i)

else:
    print("Wrong Number")
