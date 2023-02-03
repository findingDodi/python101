LEFT_CORNER_TOP = "╔"
RIGHT_CORNER_TOP = "╗"
LEFT_CORNER_BOTTOM = "╚"
RIGHT_CORNER_BOTTOM = "╝"
VERTIKAL = "║"
HORIZONTAL = "═"
output = ""

user_width = 5  # int(input("Enter width: "))
user_height = 5  # int(input("Enter height: "))

first_line = LEFT_CORNER_TOP + HORIZONTAL * user_width + RIGHT_CORNER_TOP + "\n"
last_line = LEFT_CORNER_BOTTOM + HORIZONTAL * user_width + RIGHT_CORNER_BOTTOM

output += first_line

for i in range(user_height):
    output += VERTIKAL + " " * user_width + VERTIKAL + "\n"

output += last_line

print(output)
