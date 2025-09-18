# Define function "input_registration_number()"
def input_registration_number():
    registration_number = input("Enter a registration number: ")
    if registration_number:
        return registration_number
    else:
        return None
    
# Define function "collect_registration_numbers()"
def collect_registration_numbers():
    reg_numbers = []
    while True:
        registration_number = input_registration_number()
        if registration_number is None:
            break
        reg_numbers.append(registration_number)
    return reg_numbers

# Define function "sort_registration_numbers(numbers)"
def sort_registration_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers
    
# Define function "display_sorted_numbers(numbers)"
def display_sorted_numbers(numbers):
    for number in numbers:
        print(number)

# Define function "main()"
def main():
    numbers = collect_registration_numbers()
    sorted_numbers = sort_registration_numbers(numbers)
    display_sorted_numbers(sorted_numbers)

# Start main
if __name__ == "__main__":
    main()