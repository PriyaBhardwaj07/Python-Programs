# GENERATORS ARE THE FUNCTION THAT RETURNS ITERATOR USING YIELD KEYWORD 

'''
Unlike lists and tuples, generators do not store all the values in memory at once. Instead, they generate 
values on-the-fly as you iterate over them.This makes generators more memory-efficient.

When a generator function is called, it returns an iterator called a generator object.
The generator object can be iterated using a for loop, or its values can be retrieved 
one at a time using the next() function
Generator's main benefit is that they automatically create the functions __iter__() and next ()


'''
        #yield keyword is similar to return keyword 
                # GENERATORS ARE THE FUNCTION THAT RETURNS ITERATOR USING YIELD KEYWORD 
        # Python generator functions allow you to declare a function that behaves like an iterator
  # return vs yield      
'''
def abc():
        print("executes")
        return      # here if you will not write anything after return then it will print None implicitly
        # return "dddd"
        print("not executed")
        # if want can also create object and then print
#g= abc()
#print(g)
abc() 

# BASIC EXAMPLE 
def func():
    yield 1
    yield 2
    yield 3
    yield 4
    
for x in func():
    print(x)
'''
# using next keyword
'''

def func():
    yield "hii"
    yield "pop"
    
f = func()
print(next(f))
print(next(f))


# SUM OF FIBONACCI SERIES TILL N 
def fib(n):
    if n==0:
        return 0
    elif n ==1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10)) 
'''
def gen(n):
    a=0
    while a<n:
        yield a
        #a +=1
        a= a+1
for x in gen(5):
    print(x)


def gen():
    for i in range(0,6):
        yield i*2
    
for j in gen():
    print(j)

   
# OR
# same as above code
def gen():
    for i in range(0,6):
        k= i*2
        print(k)
gen()
    

        
        