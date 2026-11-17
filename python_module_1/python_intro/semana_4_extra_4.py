#Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (primero y segundo) y los ordene de menor a mayor en dichas variables.

number_one = int(input("Ingrese el primer numero: "))
number_two = int(input("Ingrese el segundo numero: "))

if number_one > number_two:
    print(f'El numero mayor es {number_one} y el menor es {number_two}')
else:
    print(f'El numero mayor es {number_two} y el menor es {number_one}')