#Cree una función que le de la vuelta a un string y lo retorne.

def reverse_string():
    my_string = input("Tell me something?")
    for letter in range(len(my_string)-1,-1,-1):
        print(my_string[letter])

reverse_string()
