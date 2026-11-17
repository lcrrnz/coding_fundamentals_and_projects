#Cree un programa que le pida tres números al usuario y muestre el mayor.

numer_one = int(input("Ingrese el primer valor: "))
numer_two = int(input("Ingrese el segundo valor: "))
numer_three = int(input("Ingrese el tercer valor: "))
highest = 0

if numer_one > highest:
    highest = numer_one 
if numer_two > highest:
    highest = numer_two
if  numer_three > highest:
    highest = numer_three 
print(f'El numero mayor es {highest}')

