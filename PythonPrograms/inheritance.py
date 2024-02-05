"""
class food():
    def __init__(self):
        print("food")
    def eat(self):
        print("eat")
    def swim(self):
        print("swim")
        
class foo(food): # same as extends in java
    def __init__(self):
        super().__init__()
        print("foo")
    def who(self):
        print("po")

a=foo()
a.eat()
a.swim()
a.who()
"""
# SINGLE INHERITANCE:

class Parent:
    def eat(self):
        print("parent eat")
class Child(Parent):
    def eat(self):
        print("child eats")

p=Parent()
c=Child()
p.eat()
c.eat()

# MULTIPLE INHERITANCE
"""
class A:
    def disA(self):
        print("First")
class B:
    def disB(self):
        print("Second")
class C(A,B):
    def disC(self):
        print("Third")
c=C()
c.disA()
c.disB()
c.disC()
"""
# HIERARCHICAL INHERITANCE
"""
class A:
    def disA(self):
        print("First")
class B(A):
    def disB(self):
        print("Second")
class C(A):
    def disC(self):
        print("Third")
b=B()
c=C()
b.disA()
b.disB()
c.disC()
"""
# MULTILEVEL INHERITANCE
"""
class A:
    def dis(self):
        print("First")
class B(A):
    def disB(self):
        print("Second")
class C(B):
    def disC(self):
        print("Third")
c=C()
c.dis()
c.disB()
c.disC()
"""
# HYBRID INHERITANCE
# MIX OF ANY TWO(MINIMUM) INHERITANCE








