# Define function "inches_to_cm(inches)"
def inches_to_cm(inches):
    return inches * 2.54

# Define function "format_output(inches, cm)"
def format_output(inches, cm):
    return f"{inches} tuumaa on {cm:.2f} cm"

# Define function "main()"
def main():
    inches = float(input("Anna tuumamäärä: "))
    cm = inches_to_cm(inches)
    result = format_output(inches, cm)
    print(result)

# Start main
if __name__ == "__main__":
    main()