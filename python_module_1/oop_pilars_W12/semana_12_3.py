#Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.
#nos puede ser muy útil cuando tengamos clases que se parecen entre sí pero tienen ciertas particularidades

class Madre():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print("Mi nombre es", self.nombre, "y tengo", self.edad, "años de edad")

mimadre = Madre("Johanna", "30")
mimadre.presentarse()

class Padre(Madre):
    pass

mipadre = Padre("Ariel", "31")
mipadre.presentarse()