#1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.Debe incluir:Nombre,Género,Desarrollador, Clasificación ESRB

import csv

def create_dictionary():
    games_list = []
    print ("Enter games information in the following format:\n name: Grand Theft Auto IV \n genre: action \n developer: Rockstar Games \n ESRB: M")
    while True:
        try:
            user_dict ={}
            key_name = "name"
            value_name = input("Enter the game name: ") 
            user_dict[key_name] = value_name

            key_genre = "genre"
            value_genre = input("Enter the game genre: ") 
            user_dict [key_genre] = value_genre

            key_developer = "developer"
            value_developer = input("Enter the game developer: ") 
            user_dict [key_developer] = value_developer
            
            key_esrb ="esrb"
            value_esrb = input("Enter the game ESRB: ") 
            user_dict [key_esrb] = value_esrb
            
            games_list.append(user_dict)

            next_input = input("Do you want to continue? Yes/ No: ").lower()
            if next_input != 'yes':
                break
        except TypeError as error:
            print(f'Erro due to {error}')
    return games_list


def csv_writer(file_path, data, keys):
    try:
        with open (file_path,'w',newline="") as file:
            write = csv.DictWriter(file,keys)
            write.writeheader()
            write.writerows(data)
    except PermissionError as error:
        (print(f'Unable to create file due to {error}'))


def main():
    while True:
        try:
            dic_keys =(
            'name',
            'genre',
            'developer',
            'esrb',
            )
            create_file = ("game_info.csv")
            user_dictionary= create_dictionary()
            print(user_dictionary)            
            print("Creating CSV with the information provided...")
            csv_writer(create_file,user_dictionary,dic_keys)
            break
        except Exception as error:
            print(f'An unexpected error occurred, Reason:{error}')
            if error:
                restart = input("Do you want to restart? Yes/ No")
                if restart != "yes":
                    break
    print("File successfully created.")



main ()