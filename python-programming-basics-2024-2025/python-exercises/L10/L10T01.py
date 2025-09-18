import os
from collections import Counter

# Define the path and file name
path = r"F:\JAMK\Digiosaaja 2.9.2024-31.7.2025"
filename = "nimet.txt"

# List of names to be written to the file
names = [
    "Waltteri", "Iida", "Aapeli", "Calle", "Perttu", "Heikki", "Kalle",
    "Bella", "Ville", "Aapeli", "Diana", "Greta", "Iida", "Nacke", "Teppo",
    "Oona", "Satu", "Aapeli", "Fiona", "Riina", "Johan", "Kalle", "Perttu",
    "Q", "Calle", "Bella", "Micke", "Kalle", "Unna", "Eero", "Laura"
]

# Check if the directory exists, and create it if not
if not os.path.exists(path):
    os.makedirs(path)

# Create the file path by joining the directory and file name
file_path = os.path.join(path, filename)

# Write the names list to the file, one name per line
try:
    with open(file_path, 'w') as file:
        file.writelines(f"{name}\n" for name in names)
except PermissionError as e:
    raise PermissionError(f"Ei oikeuksia kirjoittaa tiedostoon: {file_path}") from e
except IsADirectoryError as e:
    raise IsADirectoryError(f"Polku osoittaa kansioon, ei tiedostoon: {file_path}") from e
except OSError as e:
    raise OSError(f"Järjestelmävirhe tiedoston kirjoittamisessa: {e}") from e

# Function to read names from the file and return them as a list
def read_names_from_file(file_path: str) -> list[str]:
    try:
        with open(file_path, "r") as file:
            names = [line.strip() for line in file]
            return names
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Tiedostoa ei löytynyt polusta: {file_path}") from e
    except PermissionError as e:
        raise PermissionError(f"Ei oikeuksia lukea tiedostoa: {file_path}") from e
    except IsADirectoryError as e:
        raise IsADirectoryError(f"Polku osoittaa kansioon, ei tiedostoon: {file_path}") from e
    except OSError as e:
        raise OSError(f"Järjestelmävirhe tiedoston lukemisessa: {e}") from e

# Function to count the total number of names in the list
def count_names(names: list[str]) -> int:
    return len(names)

# Function to count occurrences of each name in the list
def count_name_occurrences(names: list[str]) -> dict[str, int]:
    return dict(Counter(names))

# Function to print total names and their occurrences
def print_name_statistics(total_count: int, name_occurrences: dict[str, int]) -> None:
    print("Nimien kokonaismäärä:", total_count)
    # print("Nimien esiintymiskerrat:")
    for name, count in name_occurrences.items():
        print(f"{name}: {count}")

# Define main function
def main():
    try:
        names = read_names_from_file(file_path)
        total_count = count_names(names)
        name_occurrences = count_name_occurrences(names)
        print_name_statistics(total_count, name_occurrences)
    except Exception as e:
        print(f"Virhe: {e}")

# Start main
if __name__ == "__main__":
    main()