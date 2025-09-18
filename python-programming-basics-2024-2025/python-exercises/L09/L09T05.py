# Custom exception for invalid index input
class InvalidIndexError(Exception):
    pass

# Custom exception for empty string input
class EmptyStringError(Exception):
    pass

# Validate that the index is within the acceptable range
def validate_index(index: int, max_index: int) -> None:
    if not (0 <= index < max_index):
        raise InvalidIndexError(f"Indeksin tulee olla välillä 0 - {max_index - 1}.")

# Validate that the string is not empty or just whitespace
def validate_string(s: str) -> None:
    if not s.strip():
        raise EmptyStringError("Syötteen ei tule olla tyhjä.")

# Function to insert a new string at the specified index with validation
def insert_string_with_validation(strings: list[str], index: int, new_string: str) -> list[str]:
    validate_index(index, len(strings))
    validate_string(new_string)
    strings.insert(index, new_string)
    return strings

# Define main
def main():
    strings = ["a", "b", "c", "d", "e"]
    print("Alkuperäinen lista:")
    print(strings)

    try:
        updated_strings = insert_string_with_validation(strings, 2, "f")
        print("Päivitetty lista:")
        print(updated_strings)
    except (InvalidIndexError, EmptyStringError) as e:
        print(f"Virhe: {e}")

    try:
        updated_strings = insert_string_with_validation(strings, 10, "g")
    except (InvalidIndexError, EmptyStringError) as e:
        print(f"Virhe: {e}")

    try:
        updated_strings = insert_string_with_validation(strings, 1, "")
    except (InvalidIndexError, EmptyStringError) as e:
        print(f"Virhe: {e}")

# Start main
if __name__ == "__main__":
    main()
