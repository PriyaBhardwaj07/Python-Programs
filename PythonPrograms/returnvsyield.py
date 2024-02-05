  # return vs yield  
  
# return   - it terminates the function after it is written that means nothing would be printed after that 
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
'''
# yield - the yield statement only pauses the execution of the function

def abc():
    yield 1
    print("1 is printed")
    yield 2
    print("2 is also printed")
    yield 3 
    print("3 is also printed")
    
a=abc()
for x in a:
    print(x)

