# Ask the user for two integers
number1 = int(input("Anna ensimmäinen kokonaisluku: "))
number2 = int(input("Anna toinen kokonaisluku: "))
number3 = int(input("Anna kolmas kokonaisluku: "))

# Check which number is the biggest and print it
if number1 > number2 and number1 > number3:
    print(f"Suurin: {number1}")
elif number2 > number1 and number2 > number3:
    print(f"Suurin: {number2}")
elif number3 > number1 and number3 > number2:
    print(f"Suurin: {number3}")
else:
    print(f"Suurin: {number1}")