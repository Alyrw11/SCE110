
women = int(input("How many women?"))
men = int(input("how many men?"))

total = men + women

enough_players = total >= 7
enough_women = women >= 4

if enough_players and enough_women:
    print("You can play.")
else:
    print("You can't play.")

if not enough_players:
    print("You can't play but you can practice.")
