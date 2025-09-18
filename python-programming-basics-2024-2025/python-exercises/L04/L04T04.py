# Ask the user for their first name and last name
first_name = input("Anna etunimi: ")
last_name = input("Anna sukunimi: ")

# Find out the length of the given first name
name_length = len(first_name)

# Isolate the first letter of the given name
first_letter = first_name[0]

# Multiply the first letter of the name (a string) by the length of the name
# This repeats the first letter as many times as the name's length
letter_multiplication = first_letter * name_length

# Reverse last name
reversed_last_name = "".join(reversed(last_name))

# Print the repeated first letter and the reversed last name
print(f"{letter_multiplication} {reversed_last_name}")