#Need to separate the csv into sections
with open("life-expectancy.csv") as world:
    records = []    
        
    for mundo in world:
        sections = mundo.strip().split(",")
        if len(sections) >= 4 and sections[3].replace('.', '', 1).isdigit():
            entity, code, year, life_expectancy = sections[0], sections[1], int(sections[2]), float(sections[3])
            records.append((entity, code, year, life_expectancy))

#Create the min and max records using a lambda

min_record = min(records, key=lambda record: record[3])
max_record = max(records, key=lambda record: record[3])


print("What is the year and country that has the lowest life expectancy in the dataset?")
print(f"The overall minimum life expectancy was: {min_record[3]} from {min_record[0]} in {min_record[2]}")
print('What is the year and country that has the highest life expectancy in the dataset?')
print(f"The overall maximum life expectancy was: {max_record[3]} from {max_record[0]} in {max_record[2]}")

# User can enter data until they get tired

searching = True
while searching:
    time_line = input("Enter the year you are curious about:").strip().lower()

    if time_line.isdigit():
        time_line = int(time_line)
        year_records = [record for record in records if record[2] == time_line]
            
        if year_records:
            avg_life_expectancy = sum(record[3] for record in year_records) / len(year_records)
            min_year_record = min(year_records, key=lambda record: record[3])
            max_year_record = max(year_records, key=lambda record: record[3])
                
            print(f"For the year {time_line}:")
            print(f"The average life expectancy in {time_line} was {avg_life_expectancy:.2f}")
            print(f"The country with the minimum life expectancy in {time_line} was {min_year_record[0]} with {min_year_record[3]}")
            print(f"The country with the maximum life expectancy in {time_line} was {max_year_record[0]} with {max_year_record[3]}")
  
        else:
            print(f"No data available for the year {time_line}.")
    else:
        print("Please enter a valid year.")

#Instead of just askingn the time_line input right away. Question to check another year or end the program is asked.

    while searching:
        time_line2 = input("Would you like to check another year? (yes/no)? ").strip().lower()
        if time_line2 == "yes":
            break
        elif time_line2 == "no":
            print("Thank you for searching! Goodbye!")
            searching = False
        else:
            print("Invalid selection. Please enter YES or NO.")