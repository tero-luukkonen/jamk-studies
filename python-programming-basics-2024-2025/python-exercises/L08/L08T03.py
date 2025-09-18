# Ask the user to input a grade between 0 and 5
# Return the grade as an integer if valid, or None if the input is empty
# If the input is not valid, the user is prompted again
def input_grade() -> int | None:
    while True:
        grade_input = input("Anna kurssiarvosana väliltä 0-5: ")
        
        if grade_input == "":
            return None

        if grade_input.isdigit():
            grade = int(grade_input)
            if 0 <= grade <= 5:
                return grade
            else:
                print("Virhe: Arvosana tulee olla välillä 0-5.")
        else:
            print("Virhe: Syöte ei ole kelvollinen arvosana. Yritä uudelleen.")
            
# Collect grades from the user by calling input_grade()
# Return a list of the collected grades
# Stop collecting when the user inputs an empty grade (None)
def collect_grades() -> list[int]:
    grades = []
    while True:
        grade = input_grade()
        if grade is None:
            break
        grades.append(grade)
    return grades

# Calculate the average of the grades
# If the list is empty, return 0.0
def calculate_average(grades: list[int]) -> float:
    if not grades:
        return 0.0
    return float(sum(grades) / len(grades))

# Display the total number of grades and the average of the grades
def display_results(grades: list[int]) -> None:
    print(f"Arvosanoja yhteensä: {len(grades)}")
    print(f"Keskiarvo: {calculate_average(grades):.2f}")

# Main function: collects grades and displays the results
def main():
    grades = collect_grades()
    display_results(grades)

# Start main
if __name__ == "__main__":
    main()
    
    
   




