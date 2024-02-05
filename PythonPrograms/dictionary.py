# they are used to store key value pair in python

d={1:"a",2:"b",3:"j"}
print(d)
"""
# ACCESS VALUE
print("Accessing Value : ")
print(d[1])

# We can add new key-value pairs or update existing values.
d["id"]=100
print("New key value added :")
print(d)

# update the existing value
d[1]="c"
print("Value updated : ")
print(d)

del d[3]
print("value removed : ")
print(d)

print("To get Keys ")
k=d.keys()
print(k)

print("To get Values ")
v=d.values()
print(v)

di={1:"hii",5:{2:"hj",7:"hk"}}
print(di)

"""
sq={i:i**2 for i in d}
print("Dictionary comprehension")
print(sq)

x = 5
assert x == 6 # if not true gives an assertion error
