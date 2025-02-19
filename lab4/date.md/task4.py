from datetime import datetime

date1 = datetime(2024, 2, 10, 12, 0, 0) 
date2 = datetime(2024, 2, 15, 14, 30, 0) 

difference = (date2 - date1).total_seconds()

print("Difference in seconds:", difference)
