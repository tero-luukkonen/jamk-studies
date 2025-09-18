# Initialize variables to track the count of numbers and their sum
count = 0
sum_result = 0

# Start a loop to ask for user input
while True:
    input_number = input("Anna luku: ")
    
    # If the user enters an empty string, break the loop
    if input_number == "":
        break

        
    number = int(input_number) # Convert the user input (string) to an integer
    count += 1  # Increment the count of input numbers
    sum_result += number # Add the current number to the sum_result

# Print the results
print(f"Lukuja annettu: {count}")
print(f"Lukujen summa: {sum_result}")