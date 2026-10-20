#Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “*Mayor*”.

sec_time = int(input("Ingrese el tiempo en segundos: "))
ten_min_sec = 600

if sec_time <= ten_min_sec:
    print(f' El tiempo restante es {ten_min_sec - sec_time}')
else:
    print("El tiempo es MAYOR que 10 min")