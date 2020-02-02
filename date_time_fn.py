import datetime as dt

print(dir(dt))
print("Today : ",dt.datetime.today())
print("Now : ",dt.datetime.now())
print("Now Format : ",dt.datetime.now().strftime("%d/%m/%y"))
print("UTC time : ",dt.datetime.utcnow())
print("Other : ",dt.datetime(1996,12,5,22,10))
print(dt.timedelta(18555,5545,5666556))
# Max year 9999
print("MAX Year : ",dt.MAXYEAR)
# Min year 1
print("Min Year : ",dt.MINYEAR)
print("Time :",dt.time)
print("TIme Zone : ",dt.timezone)
# W : returns week num
print("Week Num : ",dt.datetime.today().strftime("%W"))
print("Week Day : ",dt.datetime.today().strftime("%w"))
print("Day of year: ",dt.datetime.today().strftime("%j"))
print("Day of month : ",dt.datetime.today().strftime("%d"))
print("Day of week : ",dt.datetime.today().strftime("%A"))