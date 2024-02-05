"""
from abc import ABC , abstractmethod
class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass

class MyClass(MyInterface):
    def my_method(self):
        print("Implemented method")

# This would raise an error since MyAnotherClass doesn't implement my_method
class MyAnotherClass(MyInterface):
    pass
obj1 = MyClass()
obj1.my_method()
"""
'''
class abcs:
    def __init__(pri,name):
        pri.name=name
obj=abcs("PYTHON")
print(obj.name)
'''
"""
from abc import abstractmethod
class Shape:
    @abstractmethod
    def area():
        pass

class Area(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
        
a=Area(5)
print("Area of a circle is :",a.area())
"""

from abc import abstractmethod
class Main:
    @abstractmethod
    def area():
        pass
class Circle(Main):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.b*self.l

c=Circle(4,5)
print(c.area())


      
            