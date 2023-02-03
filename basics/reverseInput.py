import sys

#print(sys.argv)
#print(len(sys.argv))


def reverse_input(input_text):
    input_list = input_text.split(' ')
    input_list.reverse()
    output = ' '.join(input_list)

    return output


# copy() klappt nur bei python3
user_text_input = sys.argv.copy()
user_text_input.pop(0)
reversed_text_input = reverse_input(' '.join(user_text_input))

print(reversed_text_input)
