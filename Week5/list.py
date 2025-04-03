#clients = []

#new_client = input("New client Name: ")
#clients.append(new_client)

#for client in clients:
#    print(client)

##Loops and list##

#clients = []
#newClient = ""

#while newClient != "quit":
#    newClient = input("New client name: ")
#    if newClient != "quit":
#        clients.append(newClient)

#print("The clients are: ")
#for client in clients:
#    print(f"{client}")


##List of numbers##

pointsScored = [24, 18, 31, 42, 28]

runningTotal = 0

for amount in pointsScored:
    #runningTotal = runningTotal + amount
    runningTotal += amount

print(f"The player has scred {runningTotal} points")