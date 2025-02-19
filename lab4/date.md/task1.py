from datetime import date, timedelta

a = date.today() - timedelta(days=5)
print("Today:", date.today())
print("5 days ago:", a)
