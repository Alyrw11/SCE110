#scripture = "Rejoice evermore."
#for i in range(len(scripture)):
#    letter = scripture[i]
#    print(letter)
#for letter in scripture:
#    print(letter)
word = "commitment"
favorite = input("What is your favorite letter?")
for letter in word:
    if letter.lower() == favorite.lower():
        print(letter.upper(), end="")
    else:
        print("_", end="")
print()
