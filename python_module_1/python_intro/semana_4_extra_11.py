#Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.

counter = 1
expected_number = int(input("Cuantos numeros vas a ingresar:"))
result = float(0)

while counter <= expected_number:
    number = float(input(f'Ingrese el valor {counter}: '))
    result += number 
    print(f'el numero actual es {result}')
    counter += 1

print (f'la suma total de los numeros es {result}')