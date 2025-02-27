import re
text = input("Enter a string: ")
print(re.fullmatch(r'ab{2,3}', text) is not None)
