# Aufgabe 3
import re
import random
import os


def sanitize_string(words_string: str):
    fixed_string = words_string.lower()
    fixed_string = re.sub('[^a-z]+', ' ', fixed_string)

    return fixed_string


def get_random_file_from_directory():
    word_lists = os.listdir(path='../wordlists')
    #random_list = word_lists[random.randrange(len(word_lists))]
    random_list = random.choice(word_lists)

    return "wordlists/" + random_list


def get_random_array_from_file(amount=5, file=get_random_file_from_directory()):
    file_handle = open(file, "r")
    file_content = file_handle.read()
    file_handle.close()
    file_content = sanitize_string(file_content)
    words_from_file = file_content.split()

    random_array = []
    for i in range(amount):
        random_word = words_from_file[random.randrange(len(words_from_file))]
        random_array.append(random_word)

    return random_array


def get_random_tweet_from_array(random_array):
    while len(''.join(random_array)) >= 141:
        random_array.pop()

    print(len(''.join(random_array)))
    return ' '.join(random_array)


print("Create your own random Tweet!")
#user_amount = int(input("Pleaser enter amount of words: "))
print(get_random_tweet_from_array(get_random_array_from_file()))
