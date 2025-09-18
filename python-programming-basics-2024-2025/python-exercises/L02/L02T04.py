from datetime import datetime

# Determine the current year
year = datetime.now().year

# Ask the user for their name and year of birth
first_name = input("Anna etunimesi: ")
birth_year = int(input("Syntymävuotesi: "))

# Print the message with the user's first name and calculate their age in full years
print(f"Hei {first_name}, olet {year - birth_year} vuotta.")