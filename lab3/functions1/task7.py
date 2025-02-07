def has_33(numbs):
    i = 0
    while i < len(numbs)-1:
        if numbs[i] == 3:
            if numbs[i+1] == 3:
                return True
        i += 1
    return False

numbers = input()
numbs = numbers.split()
numbs = [int(num) for num in numbs]
print(has_33(numbs))