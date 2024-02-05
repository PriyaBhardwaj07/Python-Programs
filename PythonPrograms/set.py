a = {1,2,3,4,5}
a.remove(2)
print(a)


c={"hi",2,True,90}
c.update([1,8,47])
print(c)

z=c.discard(2)
print(c)

print(a^c) # difference
print(sorted(z)) # sort
