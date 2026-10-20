#Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba. 
#Debe leer el archivo para importar los Pokémones existentes.
#Luego debe pedir la información del Pokémon a agregar.
# Finalmente debe guardar el nuevo Pokémon en el archivo.

import json


def original_json():
    try:
        json_string = '''
        [
            {
                "name": {
                    "english": "Pikachu"
                },
                "type": [
                    "Electric"
                ],
                "base": {
                    "HP": 35,
                    "Attack": 55,
                    "Defense": 40,
                    "Sp. Attack": 50,
                    "Sp. Defense": 50,
                    "Speed": 90
                }
            },
            {
                "name": {
                    "english": "Charmander"
                },
                "type": [
                    "Fire"
                ],
                "base": {
                    "HP": 39,
                    "Attack": 52,
                    "Defense": 43,
                    "Sp. Attack": 60,
                    "Sp. Defense": 50,
                    "Speed": 65
                }
            },
            {
                "name": {
                    "english": "Squirtle"
                },
                "type": [
                    "Water"
                ],
                "base": {
                    "HP": 44,
                    "Attack": 48,
                    "Defense": 65,
                    "Sp. Attack": 50,
                    "Sp. Defense": 64,
                    "Speed": 43
                }
            }
        ]
        '''

        data_j = json.loads(json_string)  
        print(f'The pokemon list is {json_string}')
    except json.JSONDecodeError as error:
        print(f'Error due to: {error}')
    return data_j


def add_pokemon():
    pokemon_list = original_json()
    while True:
        try:
            print("Add new Pokemon:")
            new_pokemon = {
                "name": {
                    "english": input("Enter the Pokemon name: ")
                },
                "type": [
                    input("Enter the Pokemon type: ")
                ],
                "base": {
                    "HP": int(input("Enter the pokemon HP attributes: ")),
                    "Attack": int(input("Enter the pokemon Attack attributes: ")),
                    "Defense": int(input("Enter the pokemon Defense attributes: ")),
                    "Sp. Attack": int(input("Enter the pokemon Sp. Attack attributes: ")),
                    "Sp. Defense": int(input("Enter the pokemon Sp. Defense attributes: ")),
                    "Speed": int(input("Enter the pokemon Speed attributes: "))
                }
            }
            
            pokemon_list.append(new_pokemon)
            next_input = input("Do you want to continue? Yes/No: ").lower()
            if next_input != 'yes':
                break
        except ValueError as error:
            print(f'Error due to {error}')
    return pokemon_list


def create_json():
    try:
        updated_list = add_pokemon()
        conversion = json.dumps(updated_list, indent=4)  
        with open ("pokemon_info.json", "w") as file:
            file.write(conversion)
    except Exception as error:
        print(f'Unable to create file due to {error}')


def main():
    try:
        create_json()
    except Exception as error: 
        print(f'Error due to {error}')



main()