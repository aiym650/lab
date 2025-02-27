import re
text = input("Enter a string: ")
print(re.fullmatch(r'a.*b', text) is not None)
