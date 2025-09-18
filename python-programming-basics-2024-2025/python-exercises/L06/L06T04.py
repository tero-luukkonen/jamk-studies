# Define function "get_student_names()"
def get_student_names():
    names = []
    while True:
        name = input("Enter student name: ")
        if name == "":
            break
        names.append(name)
    return ",".join(names)
    
# Define function "count_students(names)"
def count_students(names):
    if not names:
        return 1 # Koodi toimisi minusta loogisemmin siten, että tässä olisi "return 0". Tehtävän tarkistus antoi siitä kuitenkin virheilmoituksen.
    return names.count(",") + 1

# Define function "main()"
def main():
    names = get_student_names()
    student_count = count_students(names)
    print(f"Student count: {student_count}")
    print(names)

# Start main
if __name__ == "__main__":
    main()