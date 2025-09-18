# Creates a dictionary representing a car with given registration number, brand, model, and year
def create_car(reg_number: str, brand: str, model: str, year: int) -> dict[str, dict[str, str | int]]:
    return {reg_number: {"brand": brand, "model": model, "year": year}}

# Adds a car dictionary to the car registry
def add_car(registry: dict[str, dict[str, str | int]], car: dict[str, dict[str, str | int]]) -> None:
    registry.update(car)

# Creates and returns an empty car registry
def create_registry() -> dict[str, dict[str, str | int]]:
    return {}

# Prints cars sorted alphabetically by brand
def print_by_brand(registry: dict[str, dict[str, str | int]]) -> None:
    sorted_cars = sorted(registry.items(), key=lambda item: item[1]["brand"])
    for reg_number, car in sorted_cars:
        print(f"{reg_number}: {car['brand']} {car['model']} ({car['year']})")

# Prints cars sorted alphabetically by registration number
def print_by_reg_number(registry: dict[str, dict[str, str | int]]) -> None:
    sorted_cars = sorted(registry.items())
    for reg_number, car in sorted_cars:
        print(f"{reg_number}: {car['brand']} {car['model']} ({car['year']})")


# Define main
def main():
    registry = create_registry()
    cars = [
        create_car("ABC-123", "Skoda", "Octavia", 2020),
        create_car("XYZ-789", "Toyota", "Corolla", 2019),
        create_car("DEF-456", "Volvo", "V60", 2021),
        create_car("GHI-789", "Ford", "Focus", 2018),
        create_car("JKL-012", "Honda", "Civic", 2022)
    ]
    for car in cars:
        add_car(registry, car)

    print("Autot merkin mukaan:")
    print_by_brand(registry)
    print("\nAutot rekisterinumeron mukaan:")
    print_by_reg_number(registry)

# Start main
if __name__ == "__main__":
    main()