# Ask the user for a number between 1 and 10
user_input = input("Anna luku väliltä 1-10: ")

# Check if the input is a valid positive integer
if user_input.isdigit():
    # Convert the input to an integer
    number = int(user_input)

    # Check if the number is in the range 1-10
    if 1 <= number <= 10:
        # Generate and print the multiplication table
        for i in range(1, number + 1): # Rows
            for j in range(1, number + 1): # Columns
                # Print the product, right-aligned with 3-character width
                print(f"{i * j:3}", end= " ")
            # Print a new line after each row
            print()
    else: 
        # Print an error message if the number is out of range
        print("Virheellinen syöte!")
else:
    # Print an error message if the input is not a number
    print("Virheellinen syöte!")