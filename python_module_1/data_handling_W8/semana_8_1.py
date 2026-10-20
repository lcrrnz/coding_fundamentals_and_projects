#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def file_read_line_by_line(path):
    item_list = []
    try:
        with open(path,"r") as file:
            for line in file.readlines():
                new_line_remove = line.strip()
                item_list.append(new_line_remove)
                print(f'Song name: {line}')
    except IOError as error:
        print (f'There was an error, reason: {error}\nPlease check the spelling')
        return None
    try:
        item_list.sort()
        print(item_list)
        return item_list
    except TypeError as error:
        print (f' Unable to sort list. Error code: {error} ')
        return None



def file_creation(sorted_list):
    print("Creating a new file...")
    file_name = input("Enter new file name + '.txt': ")
    try:
        with open(file_name, "w") as file:
            for item in  sorted_list:
                file.write(f'{item}\n')
    except OSError as error:
        print (f'There was an error, reason: {error}\nUnable to create file')
    except IOError as error:
        print (f'There was an error, reason: {error}\nUnable to create file')


def main():
    while True:
        try:
            path = input ("Enter file name with the '.txt' at the end:")
            sorted_list = file_read_line_by_line(path)
            if sorted_list != None:
                file_creation(sorted_list)
            break
        except Exception as error:
            print(f'Unexpected error, reason: {error}')
            break


main()