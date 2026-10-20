#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

bikes_list = [
    "Yamaha",
    "BMW",
    "Husqvarna",
    "Ducati",
    "Suzuki",
    "KTM"
    ]

print(f'Estas es mi lista de las mejores motos {bikes_list}')

bikes_list [0]= input("Ingrese una Marca que deberia estar de primera:")
bikes_list [-1] = input("Ingrese una Marca que deberia estar al final:")

print(bikes_list)

#other way to do it 
my_list = []

counter = 1

entries = int(input("How many items are you adding?"))

while counter <= entries:
    my_list.append(input(f'add the item number {counter}:'))
    counter += 1

print(f' La lista se ve asi: {my_list}')

change_characters = int(input("Do you want to change the first and last entry? 1 yes / 2 no"))
if change_characters == 1:
    my_list[0]= (input("Add a new value for the first item:"))
    my_list[-1] = (input("Add a new value for the last item:"))
    print(f'Su lista es {my_list}')
else:
    print(f'Su lista es {my_list}')