# Define function "get_fuel"
def get_fuel(distance, consuption_100km):
    fuel_consumption = (distance / 100) * consuption_100km
    return f"{fuel_consumption} ltr"
    
# Test the function "get_fuel"
print(get_fuel(100, 7.5))
print(get_fuel(220, 6.9))