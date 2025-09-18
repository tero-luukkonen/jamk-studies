# Ask the user for their full name
full_name = input("Anna nimesi: ")

# Find space
space = full_name.find(" ")

# Separate first name and last name
first_name = full_name[:space]
last_name = full_name[space + 1:]

# Print first name and last name separately
print(f"Etunimesi: {first_name}")
print(f"Sukunimesi: {last_name}")