#4.Given threeintegers, print the smallestone.(Three integers should be user input)
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if num1< num2 and num1<num3:
    print(f" the smallest number is {num1}")
if num2 < num1 and num1 < num3:
    print(f" the smallest number is {num2}")
if num3 < num2 and num3 < num1:
    print(f" the smallest number is {num3}")



