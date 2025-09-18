# Create the "Mobile" class
class Mobile:
    #brand = ""
    #model = ""
    #price = ""

# Define the constructor "__init__" to initialize the attributes
    def __init__(self, brand, model, price, nakki):
        self.brand = brand
        self.model = model
        self.price = price
        self.nakki = nakki

# Use "__str__" method to define how the object is printed
    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Nakki: {self.nakki}"

# Create two new "Mobile" objects    
phone1 = Mobile("Samsung", "Galaxy", 349, "hyvä nakki")
phone2 = Mobile("Apple", "iPhone 12", 899, "")

# Print the created objects
print(phone1)
print(phone2)




