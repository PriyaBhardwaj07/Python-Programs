"""
x=5
y=0
try:
    if x%y:
        print("Match")
except ZeroDivisionError:
    print("Error")
    
"""
"""
# extracting email
import re 
def extract_emails(email):
  pattern = re.compile(r'^[A-Za-z]+[A-Za-z0-9._-]+@[A-Za-z]+\.(com|org|net)$')
 
  match = pattern.finditer(email)
  for m in match:
    print(m)
text = "Contact us at john.doe@example.com or support@company.org for assistance."
result = extract_emails(text)
print(result)

import re
 
def extract_emails(email):
  pattern = re.compile(r'^[A-Za-z]+[A-Za-z0-9._-]+@[A-Za-z]+\.(com|org|net)$')
 
  match = pattern.findall(email)
  return match
text = "Contact us at john.doe@example.com or support@company.org for assistance."
result = extract_emails(text)
print(result) # NOT THE DESIRED RESULT
"""
import re

def extract_emails(email):
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    match = pattern.findall(email)
    return match

text = "Contact us at john.doe@example.com or support@company.org for assistance."
result = extract_emails(text)
print(result)


