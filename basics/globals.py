class Animal:
    def __init__(self):
        self.name = "No Name"


def change_name(pet):
    # global pet
    print(pet.name)
    pet.name = "Maus"
    # pet = "No"
    print(pet.name)


def change_text(text):
    print(text)
    text = "Hamster"
    print(text)


pet = Animal()
pet.name = "Hamster"

print(pet.name)

change_name(pet)

print(pet.name)

my_text = "Cat"
change_text(my_text)
print(my_text)
