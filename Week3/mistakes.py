#x = int(input("What ist he value of x?"))
#if x == 5 or x == 6:
#    print("x is 5 or 6")

#age = input("What is your age?")
#ageNumber = int(age)
#if ageNumber < 18:
#    print("You are not old enough to vote.")
#else:
#    print("You are old enough to vote.")

rewards = 0
choice = "drink"
total = 3

if (choice == "drink" or choice == "cookie") and total > 5:
    rewards += 5

print(f"You have {rewards} reward points.")