# Define function "celToFah(cel)"
def celToFah(cel):
    fah = (cel * 9/5) + 32
    return round(fah, 1)

# Define function "fahToCel(fah)"
def fahToCel(fah):
    cel = (fah - 32) * 5/9
    return round(cel, 1)

# Define function "main()"
def main():
    # User input celsius -> fahrenheit
    cel = float(input("Anna lämpötila Celsius-asteina: "))
    print(f"{cel} °C = {celToFah(cel)} °F")
    
    # User input fahrenheit -> celsius
    fah = float(input("Anna lämpötila Fahrenheit-asteina: "))
    print(f"{fah} °F = {fahToCel(fah)} °C")

# Start main
if __name__ == "__main__":
    main()