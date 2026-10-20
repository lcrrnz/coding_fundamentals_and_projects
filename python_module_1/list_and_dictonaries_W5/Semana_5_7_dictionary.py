#2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

list_a = ["first_name", "last_name", "role"]
list_b = ["Luis", "Carranza", "Fraud Investigator"]

new_dictionary = {}

for value in range (len(list_a)):
    new_dictionary[list_a[value]] = list_b[value]

print(new_dictionary)