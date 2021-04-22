'''If name is less than 3 characters long- name must be at least 3 characters otherwise if it is more than 50 character'''
'''- name must be maximum of 50 characters otherwise -name looks good '''
name=input("enter your name: ")
if len(name)<3:
    print("name too short")
elif len(name)>=3 and len(name) <=50:
    print("name looks good")
else:
    print("name length exceeds maximum limit")