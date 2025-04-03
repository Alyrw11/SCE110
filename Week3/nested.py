temp = float(input("what is the current temperature?"))

if temp < -20:
   print("It's super freezing. Don't go outside.")
elif temp < 5:
    weather = input("what is the weather like?")

    if weather == "snow":
        print("If you are dedicated go and run, if not stay home.")
    elif weather == "rain":
        print("You can do it! Go for a run.")
    elif weather == "sunny":
        print("There is not a valid reason for you NOT to go for a run.")
    else:
        print("stop being lazy and go run.")

else:
    print("Run Forest, run!")

