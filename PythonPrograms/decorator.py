'''
decorators are a powerful and flexible way to modify or extend the behavior of functions or methods 
without changing their core implementation. 

'''
'''
def dec1(func):
    def abc():
        print("hii")
        func()
        print("hello")
    return abc()
@dec1
def bd():
    print("another")
# b = dec1(bd) # this line is used to do that same thing that @dec1 does 
    
'''
'''
def deco(func):
    def new():
        func() # existing functionality
        # add new functionality
        print("Map")
    return new
@deco  
def display():
    print("User ")
    print("USER")
    # print("Python")
# instead of writing this
#d =deco(display)
#d()
display() 

'''
"""
def decor(add):
    def wrapper():
        result = add()
        c = int(input("num3 enter : "))
        result = result + c
        print("result is ", result) 
    return wrapper
@decor
def add():
    a = int(input("num1 enter : "))
    b = int(input("num2 enter : "))
    result = a + b
    return result

#ad = decor(add)
#ad()
add()
"""
# TYPES OF DECORATORS
'''
# 1. FUNCTION DECORATORS
def dec(func):
    def new():
        func()
        print("Python")
    return new

@dec
def display():
    print("Hii")
    print("User")
#d=dec(display)
#d()
display()
'''
# 2. CLASS DECORATORS
"""
def fun(fa):
    fa.old="inside class"
    return fa
@fun
class MyClass:
    pass

m = MyClass()
print(m.old)
"""
# 3. PROPERTY DECORATOR 
# We can either use @property or we can use property()
# works same as getter and setter in other languages
# it has method getter and setter 








