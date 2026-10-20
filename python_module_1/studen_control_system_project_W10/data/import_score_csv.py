import csv

def find_and_read_file(path):
    data_dic=[
    ]
    try:
        with open (path,"r") as file:
            reader = csv.DictReader(file, delimiter=",")
            data_dic = list(reader)
        print(f"CSV file '{path}' successfully imported!")
    except FileNotFoundError:
        print(f"No previous CSV file found or data could not be imported. '{path}' was not found.")
        return []
    except Exception as error:
        print(f"Something went wrong while importing data: {error}")
        return []
    return data_dic

