"""
a="Hello\tWorld"
print(a)
print("========================")
a="Hello\nWorld"
print(a)
# if you want to print escape characters also then you can nullify them by using \\ 
# EXAMPLE 

a="Hello\nWorld"
print("\\n have been used here ", a) # if use \n then it would be can escape character and would be printed in next line

a="Py\rthon"
print(a)

"""
a={1:"A",2:"B",3:"C"}
for key,value in a.items():
    print(f"{key},{value}")