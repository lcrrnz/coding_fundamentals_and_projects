#3. Cree un programa que use una lista para eliminar keys de un diccionario.

list_of_keys = ["access_level", "age"]
employee = {
    "name": "John",
    "email": "john@ecorp.com",
    "access_level": 5,
    "age": 28
}

deleted_item_1 = employee.pop("age") 
deleted_item_2 = employee.pop("access_level") 

print(employee)

print(f' the deleted items are {deleted_item_1} and {deleted_item_2}')