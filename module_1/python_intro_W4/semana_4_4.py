#Dada `n` cantidad de notas de un estudiante, calcular: 1.Cuantas notas tiene aprobadas (mayor a 70). 2.Cuantas notas tiene desaprobadas (menor a 70). 3.El promedio de todas.4.El promedio de las aprobadas. 5.El promedio de las desaprobadas.

total_de_notas = int(input("Ingese la cantidad de notas:"))
contador_de_notas = 1
cantidad_de_notas_aprobadas = int()
cantidad_de_notas_desaprobadas = int()
promedio_de_notas_aprobadas = int()
promedio_de_notas_desaprobadas = int()
promedio_de_notas_total = int()

while contador_de_notas <= total_de_notas:
    print(f'Ingrese la nota numero {contador_de_notas}')
    nota_actual= int(input("Valor de la nota"))
    if nota_actual < 70:
        cantidad_de_notas_desaprobadas = cantidad_de_notas_desaprobadas + 1
        promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas + nota_actual
    else:
        cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
        promedio_de_notas_aprobadas = promedio_de_notas_aprobadas + nota_actual
    promedio_de_notas_total = int(promedio_de_notas_total + (nota_actual / total_de_notas))
    contador_de_notas = contador_de_notas + 1

if promedio_de_notas_desaprobadas < 0 :
    promedio_de_notas_desaprobadas = int(promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas)
if promedio_de_notas_aprobadas < 0 :
    promedio_de_notas_aprobadas = int(promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas)

print(f'El estudiante tiene esta cantidad de notas aprobadas {cantidad_de_notas_aprobadas}')
print(f'El promedio de notas aprobadas es {promedio_de_notas_aprobadas}')
print(f'El estudiante tiene esta cantidad de notas desaprobadas {cantidad_de_notas_desaprobadas}')
print(f'el promedio de notas desaprobadas es {promedio_de_notas_desaprobadas}')
print(f'El promedio de notas total es {promedio_de_notas_total}')