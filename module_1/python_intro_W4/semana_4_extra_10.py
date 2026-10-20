#Cree un diagrama de flujo que le pida un numero al usuario y muestre “Fizz” si es divisible entre 3, “Buzz” si es divisible entre 5, y “FizzBuzz” si es divisible entre ambos.

number = int(input("Ingrese un numero: "))

if number % 3 == 0:
    print("Fizz")
if number % 5 == 0:
    print("Buzz")
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
else:
    print("No FizzBuzz")