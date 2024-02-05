"""

x=5
print(type(x)) #to get type of any variable

y= int(2) # casting
print(y)

a= "Jen"
A='Hen'
print(type(a))
print(type(A))

l = [1,2,3,4,5] #list 
print(l)
l[2]=7
l.append(9)
print(l) #list are mutable 


t = (1,2,'sun')
print(t)
t[0]=6 #it would give error
print(t)

s = {1,2,3}
print(s)
s.add(8) #to add element 
s.add(9) 
s.update()
print(s)


dict= {"name" : "abc", 'age' : 78}
print(dict)

z=5
n = float(z)
print(type(n)) # python converts it into integer by itself 

 # FOR LOOP
t = (3,5,2,12)
for i in t:
    print(i)



# WHILE LOOP 
i = 0
while i < 5:
    i += 1 # if written here 0 will not be printed  
    print(i)
 #  i += 1 # here 0 will be printed  

list = ["geeks", "for", "geeks"]
for i in list:
	print(i)
 
for n in range(10):
    if n == 5:
        break
    print(n)

for number in range(10):
    if number == 5:
        continue
    print(number)

#nested loop 
for i in range(5):
    for j in range(i + 1):
        print('*', end=' ') # end=' ' a space character should be used instead of the default newline 
    print()


a = 9
if (a>5):
    print("GREATER")
else:
    print("SMALLER")

a = [12, 13, 14] 
b = [x *2 for x in a] 
print(b)
 
i = 20
if (i == 10): 
	print("i is 10") 
elif (i == 15): 
	print("i is 15") 
elif (i == 20): 
	print("i is 20") 
else: 
	print("i is not present") 
"""
"""
dict= {"name" : "abc", 'age' : 78}
print(type(dict))

# RANGE
for i in range(1,10,2): # start stop step 
    print(i)
"""

# MATH LIBRARY
import math
x=6
print(math.pow(int(x),2))