# Ask the user for their first name
first_name = input("Anna etunimesi: ")

# Find out the length of the given name
name_length = len(first_name)

# Isolate the first letter of the given name
first_letter = first_name[0]

# Print the message and the first letter of the name as many times as the name has letters
print(f"Nimessäsi {first_name} on {name_length} kirjainta.")
print(first_letter * name_length)