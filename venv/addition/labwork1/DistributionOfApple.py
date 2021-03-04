#N students take k apples and distribute them among each other evenly. The remaining (the undicisible ) part remains in
#the basket. How many apples will each student get ? How many apples will remain in the basket ? The program reads the
#number N and K. It should print the two answers for the question above.

no_students=int(input("enter the number of students: "))
no_apples=int(input("enter the number of apples: "))

D = no_apples // no_students
B = no_apples % no_students

print(f"each student get {D} apples")
print(f"the remaining apples are {B}")
