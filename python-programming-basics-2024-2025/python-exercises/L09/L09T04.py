# Initialize and return a list of 5 strings
def initialize_list() -> list[str]:
    return ['one', 'two', 'three', 'four', 'five']

# Prompt the user to input an index and ensure it's within the valid range
def get_valid_index(max_index: int) -> int:
    while True:
        try:
            index = int(input(f"Syötä indeksi välillä 0 - {max_index - 1}: "))
            if 0 <= index < max_index:
                return index
            else:
                print(f"Virhe! Indeksin tulee olla välillä 0 - {max_index - 1}.")
        except ValueError:
            print("Virhe! Syötä kelvollinen kokonaisluku.")

# Prompt the user to input a non-empty string
def get_valid_string() -> str:
    while True:
        user_input = input("Syötä merkkijono: ")
        if user_input.strip():
            return user_input
        else:
            print("Virhe! Syötteen ei tule olla tyhjä.")

# Insert a new string at the specified index in the list
def insert_string(strings: list[str], index: int, new_string: str) -> list[str]:
    strings.insert(index, new_string)
    return strings

# Print the list contents as a comma-separated string
def print_list(strings: list[str]) -> None:
    print(", ".join(strings))

# Define main
def main():
    strings = initialize_list()
    print("Alkuperäinen lista:")
    print_list(strings)
    max_index = len(strings)
    index = get_valid_index(max_index)
    new_string = get_valid_string()
    updated_strings = insert_string(strings, index, new_string)
    print("Päivitetty lista:")
    print_list(updated_strings)

# Start main
if __name__ == "__main__":
    main()