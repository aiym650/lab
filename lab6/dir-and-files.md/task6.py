import string

for letter in string.ascii_uppercase:
    with open(f'{letter}.txt', 'w') as f:
        f.write(f"This is file {letter}.txt")
print("Files A.txt to Z.txt created")
