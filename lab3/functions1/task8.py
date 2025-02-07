def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

numbers = input("Enter numbers separated by spaces: ")
numbs = list(map(int, numbers.split()))
print(spy_game(numbs))