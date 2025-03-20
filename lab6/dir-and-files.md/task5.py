my_list = ['apple', 'banana', 'cherry']

with open('output.txt', 'w') as f:
    for item in my_list:
        f.write(item + '\n')
print("List written to output.txt")
