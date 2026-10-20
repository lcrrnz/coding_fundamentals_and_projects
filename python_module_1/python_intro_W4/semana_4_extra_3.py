#Cree un algoritmo que le pida un numero al usuario y muestre la suma de todos los números desde 1 hasta ese número.

number = int(input("Ingrese un numero: "))
result = int()

while number >= 1:
    print(f'El numero actual es {number}')
    result += number -1
    number = number -1

print(f'La suma de todos los numeros es {result}')