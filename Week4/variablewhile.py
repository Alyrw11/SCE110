#payment = float(input("What is the amount?"))
#penalty = 0

#while payment < 0:
#    penalty = 1.50
#    print("Sorry the payment cannot be negative.")

#    payment = float(input("What is the amount?"))

#print (f"The amount is ${payment:.2f}. The penalty is ${penalty:.2f}")

#Activity

number = float(input("Enter a positive number:"))


while number < 0:
    print ("Sorry that is a neg number try again.")
    number = float(input("Enter a positive number"))

print (f"The number is :{number}")


candy = ""

while candy != "yes":
    candy = input("May I have a piece of candy?")

print(f"Thank you.")