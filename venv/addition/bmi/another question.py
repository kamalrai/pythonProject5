#WAP to find am or pm from the time given by the user
hours=int(input("enter the current time(hours) : "))
min=int(input("enter the time (minute): "))
if hours>24:
    print("the time value is incorrect")
elif hours<=12 :
    print(f"the time is {hours}:{min} am")

elif hours>12:
    h2=hours-12
    print(f"time is {h2}:{min} pm")

