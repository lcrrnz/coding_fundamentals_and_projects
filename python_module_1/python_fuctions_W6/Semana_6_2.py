#Experimente con el concepto de scope:
#Intente accesar a una variable definida dentro de una función desde afuera.
#Intente accesar a una variable global desde una función y cambiar su valor.

def local_variable():
    local_number = 7
    print(local_number)

local_variable()

# esto da un error (NameError: name 'number' is not defined)
#result = local_number + 7 

#print(result)

global_number = 14

def calculate_sum():
    global global_number
    local_number = 14
    global_number = global_number + local_number
    print(global_number)


calculate_sum()