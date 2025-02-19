from datetime import datetime

now = datetime.now()
now_without_microseconds = now.replace(microsecond=0)

print("With microseconds:", now)
print("Without microseconds:", now_without_microseconds)
