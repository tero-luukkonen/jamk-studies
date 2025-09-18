# Ask the user for two integers
number1 = int(input("Anna kokonaisluku: "))
number2 = int(input("Anna kokonaisluku: "))

# Check which number is smaller and print it
if number1 < number2:
    print(f"Pienempi: {number1}")
elif number2 < number1:
    print(f"Pienempi: {number2}")
else:
    print(f"Pienempi: {number1}")