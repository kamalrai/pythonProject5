#WAP which accepts marks of our four subjects and gives out percentage , total marks and grade.
math=int(input("enter the marks for math: "))
physics=int(input("enter the marks for physics: "))
chemestry=int(input("enter the marks for chemestry: "))
english=int(input("enter the marks for english: "))
computer=int(input("enter the marks for computer: "))
sum=math+chemestry+english+physics+computer+math
percentage=(sum/5)
print(f"the percentage is {percentage}")
print(f"the total marks obtained is {sum}")

if percentage<40:
    print("fail")
elif percentage>=40 or percentage<60:
    print("first division")
elif percentage >= 60 or percentage<80:
    print("pass")
elif percentage >= 80 or percentage<100:
    print("distinction")