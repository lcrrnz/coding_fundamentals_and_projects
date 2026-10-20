#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número: Suma, Resta, Multiplicación, División, Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def calculator_menu():
    actual_number = float(input("Enter the initial value:"))
    
    while True:
        try:
            print(actual_number)
            menu_selection = int(input("Select 1 for sum, 2 for subtraction, 3 for multiplication, 4 for division, 5 to clear, and 6 to exit: "))
            
            if menu_selection == 1:
                expected_value = float(input("Input number to add: "))
                actual_number = number_sum(actual_number, expected_value)
            
            elif menu_selection == 2:  
                expected_value = float(input("Input number to subtract: "))
                actual_number = number_subtraction(actual_number, expected_value)
            
            elif menu_selection == 3:
                expected_value = float(input("Input number to multiply: "))
                actual_number = number_multiply(actual_number, expected_value)
            
            elif menu_selection == 4: 
                expected_value = float(input("Input number to divide by: "))
                if expected_value == 0:
                    raise ZeroDivisionError("Error: Division by zero is not allowed.")
                actual_number = number_division(actual_number, expected_value)
            
            elif menu_selection == 5:
                actual_number = 0
            
            elif menu_selection == 6:
                print("Calculator closed")
                break
            
            else:
                print("Invalid selection. Please choose a valid option.")
        
        except ZeroDivisionError as error:
            print(f'Error code: {error}')
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def number_sum(number1, number2):
    return number1 + number2


def number_subtraction(number1, number2):
    return number1 - number2


def number_multiply(number1, number2):
    return number1 * number2


def number_division(number1, number2):
    return number1 / number2


def main():
    while True:
        try:
            calculator_menu()
            break
        except Exception as error:
            print(f'Unexpected error, reason: {error}')
            retry = input("Do you want to restart the calculator? (yes/no): ")
            if retry != 'yes':
                print("Exiting the calculator.")
                break

main()

