#8.Given a three-digit number. Find the sum of its digits.
num=int(input("enter a three digit number: "))
i=num%10
num2=num//10
o=num2%10
num3=num2//10
p=num3%10
print(i)
print(o)
print(p)
num4=i+o+p
print(num4)
