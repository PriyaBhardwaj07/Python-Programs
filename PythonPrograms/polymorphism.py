# POLYMORPHISM
"""
def add(a,b):
    return a+b
print(add(2,3))
print(add(2.8,6))

print(type(2.8))

# POLYMORPHISM WITH CLASS
class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

# INSTEAD OF WRITING THIS ONE BY ONE WE CAN DIRECTLY RUN A LOOP 
obj_ind.capital()
obj_ind.language()
obj_ind.type()
obj_usa.capital()
"""

