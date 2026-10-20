#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def number_verification(func_to_decorate):
    def wrapper(*args):
        not_numbers = []
        valid_numbers = []
        for n in args:
            if not isinstance(n, (int, float)):
                not_numbers.append(n)
            else:
                valid_numbers.append(n)
            if not_numbers:
                raise ValueError(f'Invalid parameters: {not_numbers}')
        print(f'these are valid numbers {valid_numbers}')
        return func_to_decorate(*args)
    return wrapper

@number_verification
def items(*args):
    return args


items(10, 15, 3.14 , 14)
items(10, 15, "Hello World", 14)