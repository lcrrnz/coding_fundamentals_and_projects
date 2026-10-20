import csv

def csv_file_creation(file_path,data, keys):
    try:
        if not data:
            print("No student data available. Please enter students first.")
            return
        else:
            print("Exporting data. Please wait...")
            with open (file_path,'w',newline="") as file:
                write = csv.DictWriter(file,fieldnames=keys)
                write.writeheader()
                write.writerows(data)
    except PermissionError as error:
        (print(f'Unable to create file due to {error}'))

