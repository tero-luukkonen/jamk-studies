# Create the "Car" class
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

# Create three car objects with the given attributes
car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

# Print the details of each car
print("car1:", car1.brand, car1.model, car1.price)
print("car2:", car2.brand, car2.model, car2.price)
print("car3:", car3.brand, car3.model, car3.price)

# Calculate the total price of the cars
total_price = car1.price + car2.price + car3.price
print(f"Total price of the cars is {total_price}")