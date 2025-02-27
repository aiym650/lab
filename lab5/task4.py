import re
text = input("Enter a string: ")
print(re.findall(r'[A-Z][a-z]*', text))
