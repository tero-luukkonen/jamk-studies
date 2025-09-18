number1 = int(input("Anna 1.luku: "))
number2 = int(input("Anna 2.luku: "))
number3 = int(input("Anna 3.luku: "))
number4 = int(input("Anna 4.luku: "))
number5 = int(input("Anna 5.luku: "))

print("Lukujen summa on:",
      (number1 if number1 > 0 else 0) + 
      (number2 if number2 > 0 else 0) + 
      (number3 if number3 > 0 else 0) + 
      (number4 if number4 > 0 else 0) + 
      (number5 if number5 > 0 else 0))