import re
text = input("Enter a string: ")
print(re.split(r'(?=[A-Z])', text))
