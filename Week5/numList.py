numbers = []
newNumber = -1

print("Enter a list of numbers, type 0 when finished.")
while newNumber != 0:
    newNumber = int(input("Enter number: "))
    if newNumber != 0:
       numbers.append(newNumber)

total_amount = sum(numbers)

print(f"The sum is: {total_amount}")

for total in numbers:
    total_amount += total

count = len(numbers)
ave = total_amount / count

print(f"The average is: {ave}")

best = max(numbers)
        
print(f"The largest number is: {best}")

least = min(numbers)
print(f"The smallest number is: {least}")

sortedNumbers = sorted(numbers)
print(f"The sorted list is: {sortedNumbers}")