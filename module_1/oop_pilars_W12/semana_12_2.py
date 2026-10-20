#Cree una clase abstracta de `Shape` que:
# Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
# Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
# Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass 

class Circle(Shape):
    def calculate_perimeter(self, radius = 10):
        pi= 3.14
        circumference = round(2 * pi * radius,2)
        print (f'The perimeter or circumference of a circle, with radius {radius} is {circumference} cm')
        return circumference

    def calculate_area(self, radius = 10):
        pi = 3.14
        area = round(pi * radius ** 2)
        print (f'The area of a circle, with radius {radius} is {area} cm\u00B2')
        return area


class Square(Shape):
    def calculate_perimeter(self, side = 2):
        perimeter = round(4 * side)
        print (f'The perimeter of a square, with side {side} is {perimeter} cm')
        return perimeter

    def calculate_area(self, side = 2):
        area = round(side ** 2)
        print (f'The area of a square, with side {side} is {area} cm\u00B2')
        return area


class Rectangle(Shape):
    def calculate_perimeter(self, length = 2, width = 4):
        perimeter = round(2 * (length + width))
        print (f'The perimeter rectangle, with length {length} and width {width} is {perimeter:.2f} cm')
        return perimeter

    def calculate_area(self, length = 2, width = 4):
        area = round(length * width)
        print (f'The area of a rectangle, with length {length} and width {width} is {area} cm\u00B2')
        return area


shape1 = Circle()
shape1.calculate_perimeter(2)
shape1.calculate_area(5)

shape2 = Square()
shape2.calculate_perimeter(4)
shape2.calculate_area(7)

shape3 = Rectangle()
shape3.calculate_perimeter(8,5)
shape3.calculate_area(8,5)