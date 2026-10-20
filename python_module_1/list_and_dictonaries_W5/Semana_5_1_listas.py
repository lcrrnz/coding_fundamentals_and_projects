#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

bikes_list = [
    "Yamaha",
    "KTM",
    "BMW",
    "Ducati",
    "Suzuki",
    "Husqvarna"
    ]

cars_list = [
    "Toyota",
    "Nissan",
    "BMW",
    "Ferrari",
    "Mazda",
    "Ford"
    ]

for name in range( len(bikes_list)):
    print(f'{bikes_list[name]} , {cars_list[name]}')