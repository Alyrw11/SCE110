#Author: Allison R. Wright
#Date: 28.01.2025

print("Welcome to the animal guessing game.")
print("Try to guess the answer before the 5 tries are up.")

animal = "cheetah"
length = len(animal)
max_tries = 5
num_attempts = 0

correct_answer = False
word = "_ " * length

while correct_answer == False and num_attempts < max_tries:
    print("Your hint is:", word)
    attempt = input("What animal is it? ")

    if len(attempt) != length:
        print(f"Please choose a", length, "letter animal.")
        num_attempts += 1
    else:
        num_attempts += 1
        word = ""

        for i in range(length):
            if attempt[i] == animal[i]:
                word += attempt[i].upper()
            elif attempt[i] in animal:
                word += attempt[i].lower()
            else:
                 word = word + "_ "

        if word == animal.upper() and num_attempts == 1:
            correct_answer = True
            print("You're awesome! You took", num_attempts, "attempts.") 
        elif word == animal.upper():
            correct_answer = True
            print("Nice! You took", num_attempts, "attempts.") 
        else:
            print("Your guess was not correct. Try harder")


if correct_answer == False and num_attempts == max_tries:
    print("Sorry I win. The correct answer is: ", animal)