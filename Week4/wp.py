print("Welcome to the animal guessing game.")
print("Are you ready?")

animal = "cheetah"
question = input("What animal do you think it is?")

if question.lower() == animal:
    print("Awesome! To meet 2 awesome Cheetahs go to the Cleveland Zoo.")
else:
    for letter in animal:
        print("Welcome to the animal guessing game.")
print("Are you ready?")

animal = "cheetah"
question = input("What animal do you think it is?")

if question.lower() == animal:
    print("Awesome! To meet 2 awesome Cheetahs go to the Cleveland Zoo.")
else:
    for letter in animal:
        if letter.lower() in question.lower():
            print("_", end="")
        else:
            print(letter.upper(), end="")