# Define function "get_cost"
def get_cost(distance, consuption_100km, fuel_ltr_cost):
    fuel_consumption = (distance / 100) * consuption_100km
    return f"{fuel_consumption * fuel_ltr_cost:.2f} €"

# Test function "get_cost"
print(get_cost(100, 7.5, 1.88))
print(get_cost(220, 6.9, 1.88))
