LEFT_CORNER_TOP = "╔"
RIGHT_CORNER_TOP = "╗"
LEFT_CORNER_BOTTOM = "╚"
RIGHT_CORNER_BOTTOM = "╝"
VERTICAL = "║"
HORIZONTAL = "═"
output = ""

user_width = int(input("Enter width: "))
user_height = int(input("Enter height: "))

NEW_LINE = "\n"
OUTER_BOX_LINE = HORIZONTAL * user_width
INNER_BOX_LINE = " " * user_width
FIRST_LINE = "{}{}{}{}".format(LEFT_CORNER_TOP, OUTER_BOX_LINE, RIGHT_CORNER_TOP, NEW_LINE)
LAST_LINE = "{}{}{}".format(LEFT_CORNER_BOTTOM, OUTER_BOX_LINE, RIGHT_CORNER_BOTTOM)

output += FIRST_LINE

for i in range(user_height):
    output += "{}{}{}{}".format(VERTICAL, INNER_BOX_LINE, VERTICAL, NEW_LINE)

output += LAST_LINE

print(output)
