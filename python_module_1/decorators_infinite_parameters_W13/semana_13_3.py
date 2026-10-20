#Cree una clase de User que:
# Tenga un atributo de `date_of_birth`.
# Tenga un property de `age`.
# Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.
from datetime import date

class User:
    def __init__(self,date_of_birth, ):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        age_calculation =(today.year - self.date_of_birth.year -((today.month,today.day) < (self.date_of_birth.month,self.date_of_birth.day))
        )
        return age_calculation

def min_age(func_to_decorate):
    def wrapper(user):
        if user.age < 18:
            raise ValueError(f"User is underage. User is {user.age} years old")
        else:
            print(f'User overage. User is {user.age} years old')
        return func_to_decorate(user)
    return wrapper

@min_age
def age_verification(user):
    return user.age

luis = User(date(1997, 7, 14))
age_verification(luis)