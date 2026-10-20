#Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

def alphabetic_order_list ():
    string_creation = input("add a list of items, use dash (-) to separate them: ")
    user_list = string_creation.split("-")
    print(f'The list you created is {user_list}')
    user_list.sort()
    new_sting = "-".join(user_list)
    print(f'Your list in alphabetic order is {new_sting}')


alphabetic_order_list()