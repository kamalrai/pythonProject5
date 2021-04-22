'''5.For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print
‘zero’ if it is 0'''
num=int(input("ener the number to be checked: "))
if num<0:
    print(f"{num} is negative")
elif num>0:
    print(f"{num} is positive")
else:
    print(f"{num} is zero")
