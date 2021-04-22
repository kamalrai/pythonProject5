#7.Given a positive real number, print its fractional part.
import math
num=float(input("enter a positive real number: "))
i,f =math.modf(num)
print(f"the fractional part of {num} is {i}")
print(f)
