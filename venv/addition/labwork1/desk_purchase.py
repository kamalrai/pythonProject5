#5 A school decided to replace the desks in three classroom. Each desk sits two students. Given the number of students
# in each class ,print the smallest possible number of desks that can be purchased
# the program should read three integers. the number of students in each of the three classes a, b and c respectively
# in the first test there are three groups

no_student_class1 = int(input("enter the number of student in first class : "))
no_student_class2 = int(input("enter the number of student in second class : "))
no_student_class3 = int(input("enter the number of student in third class : "))

desk_class1 = (no_student_class1 // 2)
print(f"the required number of desk for the first class is {desk_class1}")
desk_class2 = (no_student_class2 // 2)
print(f"the required number of desk for the second class is {desk_class2}")
desk_class3 = (no_student_class3 // 2)
print(f"the required number of desk for the third class is {desk_class3}")

remain_class1 = (no_student_class1 % 2)
print(f"remaining desk for first class is {remain_class1}")
remain_class2 = (no_student_class2 % 2)
print(f"remaining desk for first class is {remain_class2}")
remain_class3 = (no_student_class3 % 2)
print(f"remaining desk for first class is {remain_class3}")

total_desk = desk_class1+desk_class2+desk_class3+remain_class1+remain_class2+remain_class3
print(f"the total number of desks that can be purchased are{total_desk}")
