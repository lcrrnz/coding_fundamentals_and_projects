# Analice el algoritmo de bubble_sort usando la Big O Notation.

def bubble_sort(list_to_sort):
	# Repetimos la iteración de la lista por todos los elementos para moverlos al final
    for outer_index in range(0, len(list_to_sort) - 1):
    # Usamos esta variable para revisar si hemos movido elementos
        has_made_changes = False
		# Le restamos uno al length para parar en el penultimo elemento
    # Usamos el indice exterior para restar las ejecuciones de
    # los elementos que ya estan ordenados al final
    for index in range(0, len(list_to_sort) - 1 - outer_index):
    # Guardamos los valores del elemento actual y el siguiente
        current_element = list_to_sort[index]
        next_element = list_to_sort[index + 1]

    print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}')

    # Si el actual es mayor al siguiente, intercambiamos sus posiciones
    if current_element > next_element:
        print('El elemento actual es mayor al siguiente. Intercambiandolos...')
        list_to_sort[index] = next_element
        list_to_sort[index + 1] = current_element
        has_made_changes = True

    # Si no hemos movido elementos, la lista ya esta ordenada
    if not has_made_changes:
        return

# Bubble_sort will fall under O(n**2) because the number of comparisons grows quadratically with list size. 


# Analice los siguientes algoritmos usando la Big O Notation:
# print_numbers_times_2
def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)

# print_numbers_times_2 will fall under O(n) because it will run once per n.


#check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False

#check_if_lists_have_an_equal will fall under O(n²) because each element in one list is compared to every element in the other list.growing quadratically.


#print_10_or_less_elements
def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])

#print_10_or_less_elements will fall under O(1) because the number of iterations does not dependet of input size and will always run at most 10 times.


#generate_list_trios
def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

#generate_list_trios will fall under O(n**3) because for every items in A and B, it loops through all of C. a * b * c = O(n**3)
#completed