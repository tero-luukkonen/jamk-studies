# Define function "calculate_discount(quantity)"
def calculate_discount(quantity):
    if 10 <= quantity <= 49:
        return 5
    if 50 <= quantity <= 99:
        return 10
    if quantity >= 100:
        return 15
    else:
        return 0
    
# Define function "calculate_final_price(price, quantity, discount_percentage)"
def calculate_final_price(price, quantity, discount_percentage):
    total_price = price * quantity
    discount = total_price * (discount_percentage / 100)
    final_price = total_price - discount
    return round(final_price, 2)

# Define function "main()"
def main():
    while True:
        try:
            price = float(input("Syötä tuotteen hinta: "))
            quantity = int(input("Syötä ostettava määrä: "))
            if price <= 0 or quantity <= 0:
                print("Hinnan ja määrän tulee olla positiivisia lukuja. Yritä uudelleen.")
                continue

            discount_percentage = calculate_discount(quantity)
            final_price = calculate_final_price(price, quantity, discount_percentage)

            print(f"Alennusprosentti: {discount_percentage}%")
            print(f"Lopullinen hinta: {final_price}")
            break
     
        except ValueError:
            print("Virheellinen syöte. Syötä numerot oikeassa muodossa. Yritä uudelleen.")

# Start main
if __name__ == "__main__":
    main()