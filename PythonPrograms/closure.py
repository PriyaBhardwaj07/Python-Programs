"""
closure is a nested function that helps us access the outer function's variables even
after the outer function is closed   
It helps to minimize the use of global variables   
   
"""
def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())

