def get_number_array_from_file(file="numbers.txt"):
    file_handle = open(file, "r")
    file_content = file_handle.readlines()
    file_handle.close()

    cleaned_number_array = []
    for line in file_content:
        number = int(line.rstrip())
        cleaned_number_array.append(number)

    return cleaned_number_array


user_file = input('Please enter file: ')
number_array = get_number_array_from_file(user_file)
print('Min number = ', min(number_array))
print('Max number = ', max(number_array))

