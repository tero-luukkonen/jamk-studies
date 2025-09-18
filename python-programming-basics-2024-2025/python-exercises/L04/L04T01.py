# Total amount of rain at the start of the week
total_rain = 0

# Ask rain amount per day
for day in range(7):
    rain = int(input("Anna sademäärä: "))
    total_rain += rain

# Print the total rain amount for the week
print(f"Sademäärä yhteensä: {total_rain}")