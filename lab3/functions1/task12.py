def histogram():
    numbers = list(map(int, input().split()))
    for num in numbers:
        print('*' * num)  

histogram()
