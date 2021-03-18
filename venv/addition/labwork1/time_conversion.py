#WAP to convert seconds to day, hour, minutes and seconds.
sec=int(input("enter time in seconds: "))
min=sec//60
hour=min//60
day=hour//24
print(f"time in minutes {min}")
print(f"time in hour {hour}")
print(f"time in day {day}")