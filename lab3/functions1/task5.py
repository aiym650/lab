def permute_string(string, answer=""):
    if len(string) == 0:
        print(answer)
    else:
        for i in range(len(string)):
            permute_string(string[:i] + string[i+1:], answer + string[i])

user_input = input("Enter a string: ")
permute_string(user_input)