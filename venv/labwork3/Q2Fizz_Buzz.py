'''Q.No.2 Write a function called fizz_buzzthat takes a number.If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number.'''

num=int(input("enter the number: "))

def fizz_buzz():
    if num%3==0:
        print("Fizz")
    elif num%5==0 :
        print("buzz")
    elif num%3==0 and num%5==0:
        print("FizzBuzz")
    else:
        print({num})

fizz_buzz()