#4. Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for even in range(1,len(my_list),2):
    print(my_list[even])

#other way to do it.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = []

for number in my_list:
    if number % 2 == 0:
        even_list.append(number)

print(even_list)