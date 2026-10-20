#Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos

conversion = 1000 / 3600
speed_km = int(input("Ingrese una velocidad en KM/H: "))

speed_ms = float(speed_km * conversion)

print(f'La velocidad en metros por segundo es {speed_ms} m/s') 