import re
text = input("Enter a string: ")
print(re.findall(r'\w+_\w+', text))
