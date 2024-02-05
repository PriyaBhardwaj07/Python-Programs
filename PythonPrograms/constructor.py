"""
class complex:
# in python irrespective of the class name the constructor name is always __init__
    def __init__(self) -> None: # self tells about the reference of the object
        pass


class Name:
    n="PRIYA"
    age=16
    
obj = Name()
print(obj.n)
print(obj.age)
"""
#x=88
#print(f"Value is {x}")

# constructor
# special method used to create and initialize an object of a class
# can't return any value other than none
# aim is to initialize or assign values to the data members of the class

'''
class complex:
    def __init__(self,Name,age):
        self.name =Name
        self.age= age
    def info(self):
        print(f"{self.name} and {self.age}")
a= complex("abc",44) 
#b=complex("j",3,3) # error because self is automatically taken and including that we have now 4 arguments 
a.info()
'''


"""
# TYPES
DEFAULT:  only takes self
def __init__(self):
=======================================
PARAMETRIZED : takes parameters
def __init__(self,Name,age):

""" 
# constructor is a special method that gets called when an object is instantiated.
'''
# DEFAULT CONSTRUCTOR
class fun:
    def __init__(self):
        print("---------------Default Constructor-----------")

f= fun()
'''
# PARAMETRIZED CONSTRUCTOR
"""
class fun:
    def __init__(self,name,age):
        self.name=name
        self.age=age
f=fun("abc",18)
print(f.name)
print(f.age)
"""

class fun:
    def __init__(self):
        print("---------------Default Constructor-----------")

f= fun()

"""
  1. PArametrized       
        """




        
        