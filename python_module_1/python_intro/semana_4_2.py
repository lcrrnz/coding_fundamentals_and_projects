#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

import random 

secret_number = random.randint(1,10)
number = 0

while number != secret_number:
    number= int(input("Ingrese un numero del 1 al 10: "))
    if number == secret_number:
        print("Bien hecho, adivinaste el numero.")
    else:
        print("Intentalo de nuevo")
