# #Implemente un `bubble_sort` que funcione para [Linked Lists] La lógica es la misma. Solo que intercambiar los elementos lleva su propio proceso
# Conteo de pasos (`bubble_sort_steps`)
# Modifique su implementación de `bubble_sort` para que:
# Cuente cuántas iteraciones (pasadas) realiza el algoritmo
# Cuente cuántos intercambios se hicieron en total
# validación de entrada antes de ordenar
# Cree una función que reciba una lista y valide: Que todos los elementos sean números, Que no esté vacía, Luego aplique `bubble_sort` si pasa las validaciones
# Si hay error, debe lanzar un mensaje apropiado

class Validator:
    @staticmethod
    def number_verification(func_to_decorate):
        def wrapper(item_list):
            not_numbers = []
            valid_numbers = []
            if not item_list:
                raise TypeError(f'List is empty. Closing program')
            else:
                print(f'List not empty, checking items for correct values...\n')
                for n in item_list:
                    if not isinstance(n, (int, float)):
                        not_numbers.append(n)
                    else:
                        valid_numbers.append(n)
                
            if not_numbers:
                raise ValueError(f"Invalid parameter(s) detected: {not_numbers}. Only int and float values are allowed.")
            
            print(f"These are valid numbers: {valid_numbers}")
            return func_to_decorate(valid_numbers)
        return wrapper


class NumberSort:
    @staticmethod
    def bubble_sort(fun_to_decorate):
        def wrapper (list_to_sort=[]):
            counter_changes = 0
            counter_iterations = 0
            for outer_index in range(0, len(list_to_sort) - 1):
                made_change = False
                for index in range(0 ,len(list_to_sort) -1 - outer_index):
                    counter_iterations += 1
                    current_item = list_to_sort[index]
                    next_item = list_to_sort[index + 1]
                    print(f'-- Outer loop {outer_index}, Index {index}. Current Item: {current_item}, Next Item: {next_item}')
                    if current_item > next_item:
                        print("changing items ")
                        list_to_sort[index] = next_item
                        list_to_sort[index + 1] = current_item
                        made_change = True
                        counter_changes +=1
                if not made_change:
                    print('The list is already sorted')
                    break
            print(f'\nThe list items were changed: {counter_changes} times')
            print(f'The list was iterated: {counter_iterations} times')
            print(f'Sorted List: {list_to_sort}')
            return fun_to_decorate(list_to_sort)
        return wrapper


class Node:
    data : int
    next : "Node" 

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    head = Node

    def __init__(self, head):
        self.head = head
    
    def build_linked_list_from_list(self, lst):
        if not lst:
            self.head = None
            return
        
        self.head = Node(lst[0])
        current_node = self.head
        for item in lst[1:]:
            new_node = Node(item)
            current_node.next = new_node
            current_node = new_node

    def print_structure(self):
        current_node = self.head
        print("\nLinked List Structure:")
        while current_node is not None:
            print(f'current node: {current_node.data}')
            current_node = current_node.next


validator = Validator()
@validator.number_verification
def validate_list(item_list):
    return item_list


item_sort = NumberSort()
@item_sort.bubble_sort
def sort_lowest(item_list):
    return item_list


#test = []
#test = [69,14,"hello",97,7,3.14, "world"]
test = [69,14,97,7,3.14]
#test = [3.14, 7 ,14 , 69, 97]


final_result = sort_lowest(validate_list(test))


linked_list = LinkedList(None)
linked_list.build_linked_list_from_list(final_result)
linked_list.print_structure()

#other way to do linked list