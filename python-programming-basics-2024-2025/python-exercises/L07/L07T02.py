# Create the "Human" class
class Human:
    # Define constructor "__init__" to initialize the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Use "__str__" method to define how the object is printed
    def __str__(self):
        return f"Nimi: {self.name}, Ikä: {self.age}"

# Create two new "Human" objects 
human1 = Human("Adam", 18)
human2 = Human("Eva", 18)

# Print the created objects
print(human1)
print(human2)