def unique_elements(lst):
    new_list = []
    for num in lst:
        if num not in new_list:
            new_list.append(num)
    return new_list

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Unique elements:", unique_elements(numbers))
