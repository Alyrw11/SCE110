animal = input("Enter an animal: ")
animalLC = animal.lower()


sound = ""

if animalLC == "dog":
    sound = "woof"
elif animalLC == "cat":
    sound = "meow"
else:
    sound = "I don't know what sound that animal makes"

print(f"The {animal} makes this sound: {sound}")

#adding it to github#