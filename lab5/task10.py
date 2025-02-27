import re
text = input("Enter a string: ")
print(re.sub(r'(?=[A-Z])', '_', text).lower())
