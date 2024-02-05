def fact(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return n*fact(n-1)
f=fact(5)
print(f)

# TAIL RECURSION


