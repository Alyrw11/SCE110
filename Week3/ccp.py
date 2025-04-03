score = (input("What was your score?"))
letter = input("What was your grade?").upper()
grade = int(score)


if grade >= 90 or letter == "A":
    passed = True
elif grade >= 80 or letter == "B":
    passed = True
elif grade >= 70 or letter == "C":
    passed = True
elif grade >= 60 or letter == "D":
    passed = False
else:
    passed = False    



print (f"Your grade is {letter}{grade}")


if passed:
    print("You have passed this class.")
else:
    print("You failed this time BUT you can do it, try again.")