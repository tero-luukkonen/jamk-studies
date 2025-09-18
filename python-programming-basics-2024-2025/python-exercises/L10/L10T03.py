import os

# Define the path and file names
path = r"F:\JAMK\Digiosaaja 2.9.2024-31.7.2025"
filename_int = "kokonaisluvut.txt"
filename_float = "liukuluvut.txt"

# Check if the directory exists, and create it if not
if not os.path.exists(path):
    os.makedirs(path)

# Create the file paths by joining the directory and file name
int_file_path = os.path.join(path, filename_int)
float_file_path = os.path.join(path, filename_float)

# Function that prompts the user for input and returns it as a string
def get_number_input() -> str:
    user_input = input("Syötä numero: ")
    if user_input == "":
        return ""
    else:
        return user_input

# Function that classifies the input as "int", "float", or "error"
def classify_number(input_str: str) -> str:
    try:
        int(input_str)
        return "int"
    except ValueError:
        try:
            float(input_str)
            return "float"
        except ValueError:
            return "error"

# Function that writes a number to the specified file
def write_to_file(number: str, file_path: str) -> None:
    try:
        with open(file_path, 'a') as file:
            file.write(f"{number}\n") 
    except OSError as e:
        print(f"Virhe tiedostoon kirjoittaessa: {e}")

# Function that processes user input, classifies it, and writes valid numbers to files
# Returns a tuple with the count of integers and floats
def process_numbers() -> tuple[int, int]:
    int_count = 0
    float_count = 0

    while True:
        user_input = get_number_input()
        classification = classify_number(user_input)
       
        if user_input == "":
            break
        if classification == "int":
            write_to_file(user_input, int_file_path)
            int_count += 1
        elif classification == "float":
            write_to_file(user_input, float_file_path)
            float_count += 1
        else:
            print("Virheellinen syöte. Ohjelma lopetetaan.")
            break

    return int_count, float_count
    
# Define main function
def main():
    int_file = int_file_path
    float_file = float_file_path
    int_count, float_count = process_numbers()
    print(f"Tallennettu {int_count} kokonaislukua tiedostoon {int_file}")
    print(f"Tallennettu {float_count} liukulukua tiedostoon {float_file}")
    print("Tarkista tiedostojen sisältö tekstieditorilla.")

# Start main
if __name__ == "__main__":
    main()
         