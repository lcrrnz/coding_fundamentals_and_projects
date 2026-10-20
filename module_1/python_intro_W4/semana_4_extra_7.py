#Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, y le pida al usuario adivinar ese número. El algoritm

secret_number = 7
number = 0

while number != secret_number:
    number= int(input("Ingrese un numero del 1 al 10: "))
    if number == secret_number:
        print(f'Bien hecho! El numero es {secret_number}')
    else:
        print("Intentalo de nuevo")