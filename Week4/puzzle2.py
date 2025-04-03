import random
#Author: Allison R. Wright
#Date: 30.01.2025

#Creativity 1: I added a random list of animals
#Creativity 2: I made it so it only gives 5 attempts

# Attempt 2 Comments: I added the space in between the hints and I added what I did for creativity

print("Welcome to the animal guessing game.")
print("The Category is: Felines")
print("Try to guess the answer before the 5 tries are up.")

animals = ["cheetah", "cat", "lion", "maine coon", "leopard", "tiger", "cougar", "jaguar", "panther", "bobcat", "linx", "serval", "ocelot", "caracal"]

animal = random.choice(animals)
length = len(animal)
max_tries = 5
num_attempts = 0

correct_answer = False
word = ""

for i in range(length):
    word = word + "_ "

while correct_answer == False and num_attempts < max_tries:
    print("Your hint is:", word)
    attempt = input("What animal do you think it is?")

    if len(attempt) != length:
        print(f"Please choose a", length, "letter animal.")
        num_attempts += 1
    else:
        num_attempts += 1
        word = ""
        attempt_word =""

        for i in range(length):
            if attempt[i] == animal[i]:
                word = word +attempt[i].upper() + " "
                attempt_word = attempt_word + attempt[i].upper()
            elif attempt[i] in animal:
                word = word + attempt[i].lower() + " "
                attempt_word = attempt_word + attempt[i].upper()
            else:
                word = word + "_ "
                attempt_word = attempt_word + "_"

        if attempt_word == animal.upper() and num_attempts == 1:
            correct_answer = True
            print("You're awesome! You took", num_attempts, "attempts.")
        elif attempt_word == animal.upper() and num_attempts <5:
            correct_answer = True
            print("Nice! You took", num_attempts, "attempts.") 
        elif attempt_word == animal.upper() and num_attempts == 5:
            correct_answer = True
            print("You were close to lose. It took you", num_attempts, "attempts.")
        else:
            print("Your guess was not correct. Try harder")

if correct_answer == False and num_attempts == max_tries:
    print("Sorry I win. The correct answer is: ", animal)