#Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

def spelling_check():
    total_lower = 0
    total_upper = 0
    my_string = input("Use caps and lowercase to create a sentence: ")
    
    for letter in my_string:
        if letter.islower():
            total_lower += 1
        elif letter.isupper():
            total_upper += 1
    
    print(f"There are/is {total_upper} upper case and {total_lower} lower case")

spelling_check()