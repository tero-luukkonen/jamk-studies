# Create the "Cat" class
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color 

    # Use "__str__" method to define how the object is printed
    def __str__(self):
        return f"{self.name}, color: {self.color}"

    # Define the method "miau()"
    def miau(self):
        print("Meoooooow!")
    
# Create the cat objects and assign their properties
kissa1 = Cat("Kit", "black")
kissa2 = Cat("Kat", "white")

# Print the details of the cats
print(kissa1)
print(kissa2)

# Call the miau() method for the first cat to make it meow
kissa1.miau()