'''
a = (1,2,"Sun",8,8,8)
print(tuple((enumerate(a) ))) # it tells index and value 
print(a.count(8)) # number of times 8 has occurred 

b = (1,2,3,4,5)
l =list(b)
print(l)

c=(2,[1,2],"abcde")
print(c[2][1])  # b as 2 index 1 st element
 '''
 
t=(1,2,3,4,5,6,7)
t2=("Sun","g",7,9)
print(len(t))
#print(t + t2) # concatenate
#t[0]=2 # error as we can't item in a tuple
#print(t)

# for creating single element tuple
f=(1,) # comma should be added then it will be a tuple
print(type(f))

g=(1) # not a tuple
print(type(g))

# if you want tuple comprehension you can convert tuple into list and then use it . But this would
# still be list comprehension