d=float(input("how far did you travel today (in miles)?"))
t=float(input("how long did it take you (in hours)?"))

speed=d//t
km=d*1.609
kmph=km//t
print(f"your speed was {speed} miles per hour")
print(f"your speed was {kmph} km per hour")


