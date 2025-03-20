import os

path = '.' 

print("Directories:", [d for d in os.listdir(path) if os.path.isdir(d)])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(f)])
print("All:", os.listdir(path))
