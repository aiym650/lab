import os

path = 'copy.txt' 

if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print(f"{path} deleted.")
else:
    print("Cannot delete. File not found or no access.")
