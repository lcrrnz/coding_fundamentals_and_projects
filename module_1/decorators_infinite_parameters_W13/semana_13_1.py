#Cree un decorador que haga print de los parámetros y retorno de la función que decore.


def show_params_and_return(func_to_decorate):
    def wrapper(a, b):
        print(f"The sum of {a} and {b} is")
        func_to_decorate(a , b)
        return int(a + b)
    return wrapper

@show_params_and_return
def sum_numbers(a,b):
    return a + b


print(f"Result: {sum_numbers(10, 15)}")