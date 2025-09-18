# Ask given points
points = int(input("Anna pistemäärä: "))

# Check what grade the given points get
if points == 0 or points == 1: 
    print("Arvosana: 0")
elif points == 2 or points == 3:
    print("Arvosana: 1")
elif points == 4 or points == 5:
    print("Arvosana: 2")
elif points == 6 or points == 7:
    print("Arvosana: 3")
elif points == 8 or points == 9:
    print("Arvosana: 4")
elif points == 10 or points == 11 or points == 12:
    print("Arvosana: 5")
else:
    print("Pistemäärä ei ole sallittu.")