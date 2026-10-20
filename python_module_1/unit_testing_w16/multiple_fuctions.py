# Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6 

#Cree una función que retorne la suma de todos los números de una lista.
def list_sum(num_list = []):
    total = int()   
    print(f'Your list is {num_list}')
    if not isinstance(num_list, list):
        raise TypeError (f'{num_list} is not a valid list')
    for number in num_list:
        if not isinstance(number, (int , float)):
            raise ValueError (f'{number} is not a valid number')
        total += int(number) 
    print(f'The total of your list is {total}')
    return total


# #Cree una función que le de la vuelta a un string y lo retorne.

def reverse_string(first_string = ""):
    for letter in range(len(first_string)-1,-1,-1):
        print(first_string[letter])
    return first_string


# #Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

def spelling_check(my_string = ""):
    total_lower = 0
    total_upper = 0
    for letter in my_string:
        if letter.islower():
            total_lower += 1
        elif letter.isupper():
            total_upper += 1
    
    print(f"There are/is {total_upper} upper case and {total_lower} lower case")
    return total_lower, total_upper


# #Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def alphabetic_order_list (string_creation = ""):
    user_list = string_creation.split("-")
    print(f'The list you created is {user_list}')
    user_list.sort()
    new_string = "-".join(user_list)
    print(f'Your list in alphabetic order is {new_string}')
    return new_string


#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def number_list (user_list = []):
    for number in user_list:
        if number >= 100:
            raise ValueError (f'one or more numbers are over 100 and numbers over 100 are not prime: {number}')
    return user_list


def check_prime(number):
    if number <= 1:
        return False
    
    for div in range(2,number):
        if number % div == 0:
            return False
    return True

def main(user_list):
    number_list(user_list)
    prime_list = []
    for number in user_list:
        if check_prime(number):
            prime_list.append(number)
    print(f'The prime numbers are: {prime_list}')
    return prime_list

