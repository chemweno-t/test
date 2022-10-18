import datetime as dt
current_date = dt.date.today()

print(current_date)

date1=dt.date.today()
print("year: ",date1.year)
print("month: ",date1.month)
print("day: ",date1.day)


time2 = dt.time(10, 45,30, 35667)
print(time2)

print("hour: ",time2.hour)
print("minutes: ",time2.minute)
print("seconds: ",time2.second)
print("microseconds: ",time2.microsecond)


datetime_obj = dt.datetime(2022, 10, 18, 9, 10, 53)
print(datetime_obj)
print(datetime_obj.date())
print(datetime_obj.time())


current_time = dt.datetime.now()
print(current_time)
next_new_year = dt.datetime(2023, 1, 1)
time_remaining = next_new_year - current_time
print(time_remaining)

#strf time method
current_datetime = dt.datetime.now()
print(current_datetime)
string_date = current_datetime.strftime("%A, %B %d, %Y")
print(string_date)

#strp time method
date_string = "18 october, 2022"
date_object = dt.datetime.strptime(date_string, "%d %B, %Y")
print("Date object: ",date_object)