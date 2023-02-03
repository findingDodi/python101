# Aufgabe 2

print("Please enter a term")
print("Make sure all arguments are seperated by space")
term = input("Term: ")
splitted_term = term.split()
first_number = int(splitted_term[0])
operator = splitted_term[1]
second_number = int(splitted_term[2])
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
