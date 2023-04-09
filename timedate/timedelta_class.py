import datetime as dt

oneday = dt.timedelta(days=11,hours=5,minutes=30,seconds=56,microseconds=123456)
print(oneday)

now = dt.datetime.now()
print(now)

tomorrow = now + oneday

print(tomorrow)

