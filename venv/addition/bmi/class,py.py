#wap to check if a number is an armstrong number.
num=int(input("enter num: "))
e=num
sum=0
while num>0:
    rem=num%10
    cube=rem**3
    num=num//10
    sum=sum+cube
if sum== e:
    print(f"{e} is an armstrong number")
else:
    print(f"{e} is not an armstrong number")