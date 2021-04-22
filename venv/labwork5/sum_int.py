'''10.Write a Python program to sum of three given integers.
However, if two values are equal sum will be zero.'''
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
sum=num2+num3+num1
if num2==num1 or num2==num3 or num3==num1:
    print(" sum is zero")
else:
    print(f"sum is {sum}")
