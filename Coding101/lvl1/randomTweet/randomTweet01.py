# Aufgabe 1
import re
import random


def sanitize_string(words_string: str):
    fixed_string = words_string.lower()
    fixed_string = re.sub('[^a-z]+', ' ', fixed_string)

    return fixed_string


def get_random_tweet_from_array(amount, words):
    random_array = []
    for i in range(amount):
        #random_word = words[random.randrange(len(words))]
        random_word = random.choice(words)
        random_array.append(random_word)

    return ' '.join(random_array)


file_handle = open("../../gpl.txt", "r")
file_content = file_handle.read()
file_handle.close()
file_content = sanitize_string(file_content)
words_from_file = file_content.split()

print("Create your own random Tweet")
user_amount = int(input("Pleaser enter amount of words: "))
print(get_random_tweet_from_array(user_amount, words_from_file))
