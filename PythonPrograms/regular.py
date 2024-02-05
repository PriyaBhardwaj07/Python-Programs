# REGULAR EXPRESSION 
# RegEx can be used to check if a string contains the specified search pattern.
import re
"""
pattern = re.compile(r'apple')
result = pattern.match('apple')
if result:
    print('Match found:', result.group())
else:
    print('No match')
    
"""
"""
pattern = re.compile(r"[a-m]") # it will return all the elements between a to m 
result = pattern.findall("hello world")

print(result)  # Output: ['h', 'e', 'l', 'l', 'l', 'd']
"""



