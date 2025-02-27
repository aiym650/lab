import re
text = input("Enter a string: ")
print(re.sub(r'_([a-z])', lambda m: m[1].upper(), text))
