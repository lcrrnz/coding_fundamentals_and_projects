#Cree una clase de `Circle` con:
#Un atributo de `radius` (radio).
#Un método de `get_area` que retorne su área.
class Circle:
    def __init__(self, radius = 10):
        self.radius = radius

    def get_area(self):
        area = float(3.14 * self.radius ** 2)
        return area


circle_1 = Circle()
circle_1.get_area()
print(f'The circle area with a radius of {circle_1.radius} is = {circle_1.get_area()} m2')



circle_1.radius = float(input("what's your circle's radius: "))
circle_1.get_area()
print(f'{circle_1.radius} , {circle_1.get_area()}')
print(f'The circle area with a radius of {circle_1.radius} is = {circle_1.get_area()} m2')