# Creates and returns a list of four integers.
def create_list() -> list[int]:
    return [1, 2, 3, 4]

# Attempts to modify an element at a given index; returns True if successful, False if index is invalid.
def modify_element(numbers: list[int], index: int, new_value: int) -> bool: 
    try:
        numbers[index] = new_value
        return True
    except IndexError:
        return False

# Safely prints an element at a given index; prints an error message if the index is invalid.
def safe_print_element(numbers: list[int], index: int) -> None:
    try:
        print(numbers[index])
    except IndexError:
        print("Virheellinen indeksi")

# Define main
def main():
    numbers = create_list()
    print(f"Alkuperäinen lista: {numbers}")
    if modify_element(numbers, 2, 100):
        print(f"Muokattu lista: {numbers}")
    else:
        print("Elementin muokkaus epäonnistui.")
    if modify_element(numbers, 5, 500):
        print(f"Muokattu lista: {numbers}")
    else:
        print("Elementin muokkaus epäonnistui.")

    safe_print_element(numbers, 1)
    safe_print_element(numbers, 10)

# Start main
if __name__ == "__main__":
    main()