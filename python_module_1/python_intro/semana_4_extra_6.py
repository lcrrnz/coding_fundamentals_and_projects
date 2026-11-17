#Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.

counter = 1
total_people = 6
men = int()
women = int()
total_men = int()
total_women = int()
print("Ingrese 1 para hombre y 2 para mujer. Max 6.")

while counter <= total_people:
    people = int(input(f'Ingrese la persona {counter}: '))
    if people == 1:
        men = men + 1
        counter = counter + 1
        print (f'Hay {men} hombre(s) por ahora')
    else:
        if people == 2: 
            women = women + 1
            counter = counter + 1
            print (f'Hay {women} mujer(s) por ahora')
        else:
            print ("Numero invalido")
print(f'Hay {counter - 1} personas en total')

total_men = int((men / total_people) * 100)
total_women = int((women / total_people) * 100)

print(f'El porcetange de hombres es {total_men}%')
print(f'El porcetange de mujeres es {total_women}%')