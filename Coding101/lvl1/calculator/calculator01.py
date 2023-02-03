# Aufgabe 1

first_number = int(input("first number: "))
operator = input("operator: ")
second_number = int(input("second number: "))
result = 0

if operator == "+":
    result = first_number + second_number
    print(first_number, "+", second_number, "=", result)
elif operator == "-":
    result = first_number - second_number
    print(first_number, "-", second_number, "=", result)
elif operator == "*":
    result = first_number * second_number
    print(first_number, "*", second_number, "=", result)
elif operator == "/":
    result = first_number / second_number
    print(first_number, "/", second_number, "=", result)
else:
    print("Try using a common operator...")
