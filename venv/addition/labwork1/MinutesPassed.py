#Given the integer N - the number of minutes that has passed since midnight - how many hours nad minutes are displayed
# on the 24h digital clock ?
# the program should print two numbers: The number of hours (between 0 and 23).
# For example: If N=150, then 150 minutes have passed since midnight - i.e. it is 2:30 am.
#so the program should print 2 30,

N=int (input("Enter the minutes passed since midnight: "))
hours = (N//60)
minutes = (N%60)
print(f"the hours is {hours}")
print(f"the minutes is{minutes}")
print(f"its{hours}:{minutes}")
