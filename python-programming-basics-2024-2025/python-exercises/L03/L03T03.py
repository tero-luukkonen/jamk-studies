# Ask the user for integer
number1 = int(input("Anna kokonaisluku: "))

# Check if the number is 10 or 20
if number1 == 10 or number1 == 20:
    print("Luku on 10 tai 20")
# Check if the number is 100 or 200   
elif number1 == 100 or number1 == 200:
    print("Luku on 100 tai 200")
# Otherwise, print the number
else:
    print(f"Luku on {number1}")