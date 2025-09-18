import os
import random

# Define the path and file name
path = r"F:\JAMK\Digiosaaja 2.9.2024-31.7.2025"
filename_lotto = "lotto.txt"

# Check if the directory exists, and create it if not
if not os.path.exists(path):
    os.makedirs(path)

# Create the file paths by joining the directory and file name
lotto_file_path = os.path.join(path, filename_lotto)

# Function to generate 7 random lottery numbers between 1 and 40
def generate_lottery_numbers() -> list[int]:
    return random.sample(range(1, 41), 7)
    
# Function to format a list of lottery numbers into a string
def format_lottery_numbers(numbers: list[int]) -> str:
    return " ".join(map(str, numbers))

# Function that writes the formatted lottery numbers to the specified file
def save_lottery_numbers(numbers: str, file_path: str) -> None:
    try:
        with open(file_path, 'a') as file:
            file.write(f"{numbers}\n") 
    except OSError as e:
        print(f"Virhe tiedostoon kirjoittaessa: {e}")

# Function to run the lottery process: generate, format, and save the numbers
def run_lottery() -> list[int]:
    lottery_numbers = generate_lottery_numbers()
    formatted_numbers = format_lottery_numbers(lottery_numbers)
    save_lottery_numbers(formatted_numbers, lotto_file_path)
    return lottery_numbers

# Define main function
def main():
    file_path = lotto_file_path
    try:
        lottery_numbers = run_lottery()
        print(f"Arvotut lottonumerot: {format_lottery_numbers(lottery_numbers)}")
        print(f"Numerot on tallennettu tiedostoon {file_path}")
    except Exception as e:
        print(f"Virhe: {e}")

# Start main
if __name__ == "__main__":
    main()

