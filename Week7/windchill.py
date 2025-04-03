import math

def calculate_wind_chill(temperature, wind_speed):
    # Calculate wind chill using the formula
    wind_chill = (35.74 + 0.6215 * temperature 
                  - 35.75 * (wind_speed ** 0.16) 
                  + 0.4275 * temperature * (wind_speed ** 0.16))
    return wind_chill

# Get user input
searching = True
while searching:

    temperature = float(input("Enter the temperature: "))
    location = input("Enter the location: ")
    temp_type = input("Is the temperature in Fahrenheit or Celsius? (F/C): ").strip().upper()

# Convert Celsius to Fahrenheit if necessary
    if temp_type == "C":
        temperature = (temperature * 9/5) + 32
    elif temp_type != "F":
        print("Invalid temperature type. Please enter 'F' or 'C'.")
        exit()  # Exit the program if input is invalid

# Calculate and display wind chill for wind speeds from 5 to 60 mph
    print(f"Location: {location}")
    print(f"At temperature {temperature:.1f}F:")
    for wind_speed in range(5, 65, 5):  # Loop from 5 to 60 mph 
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At wind speed {wind_speed} mph, the wind chill is: {wind_chill:.2f}F")


    while searching:
        temp1 = input("Would you like try again? (yes/no)? ").strip().lower()
        if temp1 == "yes":
            break
        elif temp1 == "no":
            print("Thank you for searching! Goodbye!")
            searching = False
        else:
            print("Invalid selection. Please enter YES or NO.")