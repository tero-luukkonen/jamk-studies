# Ask the user for a number between 1 and 10
# Use a while loop until the user provides valid input

while True:
    number = int(input("Anna numero väliltä 1-10: "))

    if 1 <= number <= 10:
        break         
    else:
     print("Luku ei ole välillä 1-10, yritä uudelleen.")

# Iterate through numbers from 1 to the user's input (inclusive)
# Print the results: the square of each number
for i in range(1, number + 1):
         print(f"Luvun {i} neliö on {i**2}")