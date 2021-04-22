'''WAP to find factorial of number by using fnction'''
def fact(num):
    num=int(input("enter the number for factorial: "))
    product = 1
    for i in range(1,num+1):
        product = product * i
    print(f"the factorial of {num} is {product}")

