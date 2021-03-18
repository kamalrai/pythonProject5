#wap to print the multiplication table of 5 to 10.
num=int(input("enter the number for multiplication: "))
for i in range(1,11):
    multiplication = num * i
    print(num,'*',i,'=',multiplication)