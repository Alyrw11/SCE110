loan = int(input("What is the loan amount?"))
creditH = int(input("What is your credit history?"))
income =  int(input("What is your income?"))
payment =  int(input("What is your monthly payment?"))

if loan >= 5:
 if creditH >= 7 and income >= 7:
    approved = True
 elif creditH >= 7 or income >= 7:
   if payment >= 5:
    approved = True
   else:
    approved = False

else:
    if creditH < 4:
        approved = False
    else: 
       if income >= 7 or payment >= 7:
        approved = True
       elif income >= 4 and payment >= 4:
        approved = True 
       else:
        approved = False

if approved:
    print("Your loan is approved.")
else:
    print("Your loan is denied.")