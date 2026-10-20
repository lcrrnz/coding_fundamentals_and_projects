# Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
#bebe 0-1 , niño 2 - 7, preadolescente 8 - 10, adolescente 11 -19, adulto joven 20 - 26, adulto 27 - 59,adulto mayor 60 +. 

name = input ("Ingrese su nombre:")
last_name = input ("Ingrese su apellido:")
age = int(input("Ingrese su edad:"))

if age <= 1:
    print(f'{name} {last_name}. Eres un bebe')
else:
    if age >= 2 and age <= 7:
        print(f'{name} {last_name}.Eres un niño')
    else:
        if age >= 8 and age <= 10:
            print(f'{name} {last_name}. Eres un preadolescente')
        else:
            if age >= 11 and age <= 19:
                print(f'{name} {last_name}. Eres un adolescente')
            else:
                if age >=20 and age <= 26:
                    print(f'{name} {last_name}. Eres un adulto joven')
                else:
                    if age >= 27 and age <=59:
                        print(f'{name} {last_name}. Eres un adulto')
                    else:
                        if age >= 60:
                            print(f'{name} {last_name}. Eres un adulto mayor')
                        else:
                            print("No hay edad")