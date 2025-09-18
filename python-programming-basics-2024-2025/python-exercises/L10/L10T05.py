# Function to write a list of names to a file
def write_names_to_file(names: list[str], file_handler) -> None:
    filename = "sukunimet.txt"
    try:
        with file_handler(filename, 'w') as file: # Open the file for writing
            for name in names:
                file.write(name + '\n') # Write each name followed by a newline character
    except Exception as e:
        print(f"Virhe kirjoitettaessa tiedostoon: {e}") # Handle any errors that occur during file writing

# Function that reads names from a file and returns them as a list
def read_names_from_file(file_handler) -> list[str]:
    filename = "sukunimet.txt"
    try:
        with file_handler(filename, 'r') as file: # Open the file for reading
            return [line.strip() for line in file.readlines()] # Return list of names without newline characters
    except Exception as e:
        print(f"Virhe tiedostoa luettaessa: {e}") # Handle any errors that occur during file reading
        return []

# Function that processes user input to collect names, write them to a file, and then read and print them
def process_names(input_func, output_func, file_write, file_read):
    # Ask the user to input names
    names = []
    while True:
        name = input_func("Anna sukunimiä (tyhjä syöte lopettaa nimien kyselyn): ")
        if name == "": # Stop on empty input
            break
        names.append(name)
     
    # Write the names to the file
    write_names_to_file(names, file_write)

    # Read the names from the file and print them
    output_func("\nTiedostoon tallennetut sukunimet:")
    read_names = read_names_from_file(file_read)
    for name in read_names:
        output_func(name)

# Define main function
def main():
    # Call the process_names function with the required functions
    process_names(input, print, open, open)

# Start main
if __name__ == "__main__":
    main()