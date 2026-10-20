#Cree un diagrama de flujo que le pida 100 números al usuario y muestre el mayor de todos.

counter = 1
highest = int()
expected_number = int(input ("Cuantos numeros vas a agregar: "))

while counter <= expected_number:
    number = float(input(f'Ingrese el valor {counter}: '))
    if number > highest:
        highest = number
    counter = counter + 1

print(f'El numero mayor es {highest}')