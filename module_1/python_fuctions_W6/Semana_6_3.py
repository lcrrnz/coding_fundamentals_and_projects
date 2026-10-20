#Cree una función que retorne la suma de todos los números de una lista.
def list_sum():
    characters = int(input("how many items are you adding? "))
    counter = 1
    list_items = []
    total = int()
    while counter <= characters:
        list_items.append(input(f'Add value number {counter}:'))
        counter += 1
    
    print(f'Your list is {list_items}')

    for number in list_items:
        total += int(number) 
    
    print(f'The total of your list is {total}')


list_sum()