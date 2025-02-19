def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Enter the starting number a: "))
b = int(input("Enter the ending number b: "))

for square in squares(a, b):
    print(square)
