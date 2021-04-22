'''Q.No.1 Write a Python function to find the Max of three numbers'''

n1=int(input("enter the first number: "))

n2=int(input("enter the second number: "))

n3=int(input("enter the third number: "))

def Fun():
    if n1>n2 and n1>n3 :
        print(f"{n1} is the max number")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} is the max number")
    else:
        print(f"{n3} is the max number")

Fun()