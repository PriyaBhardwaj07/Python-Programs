"""
# Decorators
 
Decorators are used to modify or enhance the behavior of functions or methods without changing their source code.
 
# Decorator for get request (@require_GET)
 
# Types of Decorators:
 
**Function Decorators** (Adding logging or timing functionality to a function)
**Class Decorators** (Applying a decorator to a class that enhances the behavior of its methods)
**Method Decorators** (Authenticating or authorizing access to a specific method within a class)
**Property Decorators** (Adding validation logic to a class attribute)
**Parameterized Decorators** (Passing configuration parameters to a decorator to customize its behavior)
**Multiple Decorators** (You can apply multiple decorators to a single function or method, and they will be executed in the order they are applied.)  
    
    
"""

# FUNCTION DECORATOR 
"""
def deco(func):
    def inner():
        print("---------------- FUNCTION DECORATOR ------------------")
        func()
    return inner
@deco
def display():
    print("HI")
    print("User")
    
display()
"""
# CLASS DECORATOR 

class Power(object):
    def __init__(self,arg):
        self.arg=arg
    def __call__(self,a,b):
        g=self.arg(a,b)
        return g**2
@Power
def mul(a,b):
    return a*b
print(mul)
print(mul(2,2))

#
