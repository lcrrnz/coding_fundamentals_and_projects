# Crea un `bubble_sort` por tu cuenta sin revisar el código de la lección.
# Modifica el `bubble_sort` para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        made_change = False
        for index in range(len(list_to_sort) - 1, outer_index, -1):
            current_item = list_to_sort[index]
            next_item = list_to_sort[index - 1]
            print(f'-- Index {index}. Current Item: {current_item}, Next Item: {next_item}')
            if current_item < next_item:
                print("changing items ")
                list_to_sort[index] = next_item
                list_to_sort[index - 1] = current_item
                made_change = True
        if not made_change:
            return

test_list = [87, 35, 14, 42, 93, 7]
bubble_sort(test_list)
print(test_list)