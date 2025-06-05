import datetime
x = datetime.datetime.now()
print(x.strftime("%b"))
print(x)
print(x.hour)
print(x.year)
print(x.minute)
y = datetime.date.today()
print("today is not",y)