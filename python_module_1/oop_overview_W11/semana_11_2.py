#Cree una clase de `Bus` con:
#Un atributo de `max_passengers`.
# Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).

class Bus:
    def __init__(self, max_passengers = 120):
        self.max_passengers = max_passengers
        self.current_passengers = 0
        self.available_space = 0
        self.passengers = []
    
    def add_passenger(self, person):
        try:
            if person.ticket and self.current_passengers < self.max_passengers:
                self.passengers.append(person)
                self.current_passengers += 1
                print(f"{person.name} got on the bus.")
            elif not person.ticket:
                print(f"{person.name} has no ticket and can't board.")
            else:
                print(f"The bus is full. {person.name} can’t board.")
        except Exception as error: 
            print(f'program closed due {error}')
        
    def remove_passenger(self, name):
        try:
            for person in self.passengers:
                if person.name.lower() == name.lower():
                    self.passengers.remove(person)
                    self.current_passengers -= 1
                    print(f"{name} has gotten off the bus.")
                    break
            else:
                print(f"No passenger named {name} was found on the bus.")

            if len(self.passengers) == 0:
                print("The bus dropped off all passengers. Off to the parking lot. 🅿️")
        except Exception as error:
            print(f"Program closed due to: {error}")


class Person():
    def __init__(self,name, ticket):
        self.name = name
        self.ticket = ticket


p1 = Person("Luis",True)
p2 = Person("Diego",True)

my_first_bus = Bus(2)
my_first_bus.add_passenger(p1)
my_first_bus.add_passenger(p2)
my_first_bus.remove_passenger("Luis")