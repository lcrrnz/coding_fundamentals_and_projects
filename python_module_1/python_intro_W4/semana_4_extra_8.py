#Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.

numer_one = int(input("Ingrese el primer numero: "))
numer_two = int(input("Ingrese el segundo numero: "))
numer_three = int(input("Ingrese el tercer numero: "))

if numer_one == 30 or numer_two == 30 or numer_three == 30:
    print ("Correcto! Uno de ellos es 30")
else:
    if numer_one + numer_two + numer_three == 30:
        print ("Correcto! La suma de los 3 es 30")
    else:
        print("Incorrecto! Ninguno es 30 y sumados no son 30")