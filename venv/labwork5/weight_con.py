'''weight converter :'''
'''Input the weight of a person in either lps or kg.If the person provides his/her weight in lbs convert it into kg'''
'''and vice versa '''
weight=int(input("enter your weight: "))
unit=input("enter the unit of weight: ")
if unit=="lbs":
    weight1=weight/2.20462
    print(f"the weight is {weight1} kg")
elif unit=="kg":
    weight1=weight*2.20462
    print(f"the weight is {weight1} lbs")
