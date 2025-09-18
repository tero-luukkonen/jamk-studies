# Create the "Pelikortti" class
class Pelikortti:
    def __init__(self, maa, arvo):
        self.maa = maa
        self.arvo = arvo

# Create five playing card objects with different attributes
kortti1 = Pelikortti("risti", 10)
kortti2 = Pelikortti("pata", 14)
kortti3 = Pelikortti("ruutu", 7)
kortti4 = Pelikortti("hertta", 5)
kortti5 = Pelikortti("risti", 6)

# Print the details of the cards
print(kortti1.maa, kortti1.arvo)
print(kortti2.maa, kortti2.arvo)
print(kortti3.maa, kortti3.arvo)
print(kortti4.maa, kortti4.arvo)
print(kortti5.maa, kortti5.arvo)