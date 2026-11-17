#Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.

number_one = int(input("Ingrese el primer valor: "))
number_two = int(input("Ingrese el segundo valor: "))
number_three = int(input("Ingrese el tercer valor: "))
number_four = int(input("Ingrese el cuarto valor: "))
number_five = int(input("Ingrese el quinto valor: "))

highest = int(0)

if number_one > highest:
    highest = number_one
if number_two > highest:
    highest = number_two
if number_three > highest:
    highest = number_three
if number_four > highest:
    highest = number_four
if number_five > highest:
    highest = number_five

print(f'El numero mayor es {highest}')

'''counter = 1
highest = int()
expected_number = int(input ("Cuantos numeros vas a agregar: "))

while counter <= expected_number:
    number = float(input(f'Ingrese el valor {counter}: '))
    if number > highest:
        highest = number
    counter = counter + 1

print(f'El numero mayor es {highest}')'''