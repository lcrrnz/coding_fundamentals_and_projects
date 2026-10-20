#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = "I love Yamaha"

for letter in range(len(my_string)-1,-1,-1):
    print(my_string[letter])

#print(my_string [::-1])