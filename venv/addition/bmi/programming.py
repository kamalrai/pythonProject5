#WAP to take a input from the user ,ask the user's age .If the user's age is below 18 ,print a message "acces denied in
# this site", if the user's age is greater tha 18 and lesser than 40 'print a message "access granted", if the usre's
# age is greater than 40 print a message "you are too old for this site'
print("age verification for some website")
age=int(input("enter your age: "))
if age<18:
    print("you are too young to enter this site")
elif age>18 and age<40:
    print("access granted")
else:
    print("you are too old for this site")
