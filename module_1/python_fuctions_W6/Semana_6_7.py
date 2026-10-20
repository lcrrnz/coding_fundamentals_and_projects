#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

def number_list ():
    counter = 1 
    user_list = []
    excepted_inputs = int(input("how many items are you adding?"))
    while counter <= excepted_inputs:
        user_list.append(int(input(f'add your item # {counter}: ')))
        counter += 1
    for number in user_list:
        if number >= 100:
            print (f'one of more numbers are over 100 and numbers over 100 are not prime: {number}')
    return user_list


def check_prime(number):
    if number <= 1:
        return False
    
    for div in range(2,number):
        if number % div == 0:
            return False
    return True

def main():
    user_list = number_list()
    prime_list = []
    for number in user_list:
        if check_prime(number):
            prime_list.append(number)
    print(f'The prime numbers are: {prime_list}')

main()