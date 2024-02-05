'''
__iter__() and __next__().


class sq:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration
for value in sq(5):
    print(value)
'''
"""
class func:
    def __init__(self,n): # it is not mandatory to use self you can use any other word also 
        self.n=n
        self.start= 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <=self.n:
            result= self.start *2
            self.start +=1
            return result
        else:
            raise StopIteration
for value in func(5):
    print("Value are ",value)
"""

    
