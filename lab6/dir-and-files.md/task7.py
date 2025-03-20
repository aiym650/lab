with open('testfile.txt', 'r') as src, open('copy.txt', 'w') as dst:
    dst.write(src.read())
print("Copied to copy.txt")
