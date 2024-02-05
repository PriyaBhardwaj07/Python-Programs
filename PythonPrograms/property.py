class Circle:
    def __init__(self, radius):
        self._radius = radius  # Note the use of underscore for a private attribute
        
    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return 2 * self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
"""
    @radius.deleter
    def radius(self):
        print("Deleting the radius")
        del self._radius
"""

# Usage
my_circle = Circle(5)

print(f"Radius: {my_circle.radius}")
print(f"Diameter: {my_circle.diameter}")
print(f"Area: {my_circle.area}")
print(f"Circumference: {my_circle.circumference}")
"""
my_circle.radius = 7
print(f"New Radius: {my_circle.radius}")

del my_circle.radius
"""
# Accessing radius now would raise an AttributeError since it has been deleted
