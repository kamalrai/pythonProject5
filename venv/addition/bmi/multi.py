'''WAP to print multiplication tabe of a function'''
def multi(num):
    for i in range(1,11):
        product=num*i
        print(f"{num}*{i}={product}")

num=int(input("enter the number for multiplication"))
multi()