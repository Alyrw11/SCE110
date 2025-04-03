##creativity: I after the fisrt selection of the triforce, I added more options depending on the choice of the player such as marriage, war, allies, etc.##
##creativity: The creativity and Exceeding Reques have been labeled by named instead of a choice number.##

##Author: Allison R. Wright##

print ("Welcome to the Adventure Game!")
print("Ready for your adventure to begin?")

adventure = input("You are part of the triforce, which one do you pick? COURAGE, WISDOM, or POWER?")
choice1 = adventure.lower()
if choice1 == "power":
    print("You have chosen the Triforce of Courage. You seek the ability to take over Hyrule.")
    choice2 = input("How would you conquer it? Do you get MARRIED or go to WAR?").lower()
    if choice2 == "married":
        print("You marry Zelda. You are now the king of Hyrule.")         
    elif choice2 == "war":
        print("You must defeat the hero of Hyrule.")
        war = input("How would you defeat the hero? By TRANSFORMING or using a SWORD?").lower()
        if war == "transforming":
            print("You have chosen to transform into a gigant Pig. The hero defeats you.")
        elif war == "sword":
            print("You have defeated the hero.")
        else:
            print("You have decided to retreat and live in the forest.")
    else:
        print("You decided to stay in Gerudo and rule as the rightful King.")
        
elif choice1 == "wisdom":
    print("You are the princes of Hyrule.")
    choice3 = input("How would you rule? Do you keep the PEACE or become a CONQUEROR?").lower()
    if choice3 == "peace":
        print("Hyrule is a peaceful and flourishing kingdom.")
    elif choice3 == "conqueror":
        print("You must invest in your army and take over the other kingdoms.")
        army = input("Who is in your army? ZORAS, RITO or GORON?").lower()
        if army == "zoras":
            print("You have a strong navy.")
        elif army == "rito":
            print("You have a strong air force.")
        elif army == "goron":
            print("You have a strong army.")
        else:
            print("You need better military.")
    else:
        print("Your kingdom gets taken over by Ganondorf.")


elif choice1 == "courage": 
    print("You have chosen the Triforce of Courage. You are the chosen one, the one to have the master sword.") 
    choice4 = input("How are you training? Are you using your SWORD, your BOW or are you just EATING?").lower()
    if choice4 == "sword":
        print("You're on your way to get the Master Sword.")
        sword = input("You now have the Master Sword. Do you go FIGHT Ganondorf or do the TRIALS of the Sword").lower()
        if sword == "fight":
            print("Is a hard battle but you defeat Ganondorf.")
        elif sword == "trials":
            print("The Master Sword is so powerful. The battle agains Ganon is easy.")
    elif choice4 == "bow":
        print("You are excellent with the bow, but you need to train with the sword.")
    elif choice4 == "eating":
        print("When the time comes to defend princess Zelda you lose because you didn't trained.")
    else:
        print("You changed your mind and decidedd to become a humble farmer.")
