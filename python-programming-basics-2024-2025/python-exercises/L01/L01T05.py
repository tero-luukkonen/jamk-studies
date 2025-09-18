# Prompt for the euro amount
euros = int(input("Euroja: "))

# Prompt for the cent amount
cents = int(input("Senttejä: "))

# Calculate the total amount
total_amount = euros + (cents / 100)

# Print results
print(f"Sinulla on: {total_amount:.2f} euroa")